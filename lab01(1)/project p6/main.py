# main.py
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
from datetime import datetime

from geometry_app.calculations import calculate_shape
from geometry_app.materials import get_material_names

Window.size = (800, 600)

class GeometryApp(App):
    def build(self):
        self.title = "Калькулятор геометрических тел"
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        main_layout.add_widget(Label(text="Калькулятор геометрических тел", font_size='20sp', size_hint_y=0.1))
        
        # Выбор фигуры
        shape_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        shape_layout.add_widget(Label(text="Выберите фигуру:", size_hint_x=0.3))
        self.shape_spinner = Spinner(text="Параллелепипед", values=("Параллелепипед", "Тетраэдр", "Шар"), size_hint_x=0.7)
        self.shape_spinner.bind(text=self.on_shape_change)
        shape_layout.add_widget(self.shape_spinner)
        main_layout.add_widget(shape_layout)
        
        self.inputs_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.3)
        main_layout.add_widget(self.inputs_layout)
        
        # Выбор материала
        material_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        material_layout.add_widget(Label(text="Выберите материал:", size_hint_x=0.3))
        self.material_spinner = Spinner(text="Алюминий", values=get_material_names(), size_hint_x=0.7)
        material_layout.add_widget(self.material_spinner)
        main_layout.add_widget(material_layout)
        
        # Кнопки
        buttons_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        self.calc_button = Button(text="Рассчитать", on_press=self.calculate)
        self.save_button = Button(text="Сохранить отчет", on_press=self.save_report, disabled=True)
        buttons_layout.add_widget(self.calc_button)
        buttons_layout.add_widget(self.save_button)
        main_layout.add_widget(buttons_layout)
        
        main_layout.add_widget(Label(text="Результаты:", size_hint_y=0.05, halign='left'))
        
        self.result_text = Label(text="Нажмите 'Рассчитать' для получения результатов", size_hint_y=0.35, halign='left', valign='top')
        self.result_text.bind(size=self.result_text.setter('text_size'))
        
        result_scroll = ScrollView()
        result_scroll.add_widget(self.result_text)
        main_layout.add_widget(result_scroll)
        
        self.current_shape = "Параллелепипед"
        self.update_input_fields()
        self.last_result = None
        
        return main_layout
    
    def on_shape_change(self, spinner, text):
        self.current_shape = text
        self.update_input_fields()
        self.result_text.text = "Нажмите 'Рассчитать' для получения результатов"
        self.save_button.disabled = True
        self.last_result = None
    
    def update_input_fields(self):
        self.inputs_layout.clear_widgets()
        
        # Параметры для каждой фигуры
        params = {
            "Параллелепипед": [("Длина (см):", "length"), ("Ширина (см):", "width"), ("Высота (см):", "height")],
            "Тетраэдр": [("Длина ребра (см):", "edge")],
            "Шар": [("Радиус (см):", "radius")]
        }
        
        for label_text, attr_name in params[self.current_shape]:
            self.inputs_layout.add_widget(Label(text=label_text))
            input_field = TextInput(text="10", input_filter='float')
            self.inputs_layout.add_widget(input_field)
            setattr(self, f"{attr_name}_input", input_field)
    
    def get_dimensions(self):
        dimensions = {}
        
        if self.current_shape == "Параллелепипед":
            dimensions['length'] = float(self.length_input.text or 0)
            dimensions['width'] = float(self.width_input.text or 0)
            dimensions['height'] = float(self.height_input.text or 0)
        elif self.current_shape == "Тетраэдр":
            dimensions['edge'] = float(self.edge_input.text or 0)
        elif self.current_shape == "Шар":
            dimensions['radius'] = float(self.radius_input.text or 0)
            
        return dimensions
    
    def calculate(self, instance):
        try:
            dimensions = self.get_dimensions()
            
            if any(v <= 0 for v in dimensions.values()):
                self.show_error("Ошибка", "Все размеры должны быть положительными числами")
                return
            
            shape_map = {"Параллелепипед": "parallelepiped", "Тетраэдр": "tetrahedron", "Шар": "sphere"}
            
            self.last_result = calculate_shape(shape_map[self.current_shape], dimensions, self.material_spinner.text)
            self.display_result()
            self.save_button.disabled = False
            
        except Exception as e:
            self.show_error("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def display_result(self):
        if not self.last_result:
            return
        
        r = self.last_result
        self.result_text.text = f"""
Фигура: {self.current_shape}
Материал: {r['material']}

Объем:
  • {r['volume_cm3']} см³
  • {r['volume_m3']} м³

Площадь поверхности:
  • {r['surface_area_cm2']} см²
  • {r['surface_area_m2']} м²

Масса:
  • {r['mass_g']} г
  • {r['mass_kg']} кг
"""
    
    def save_report(self, instance):
        if not self.last_result:
            self.show_error("Ошибка", "Нет результатов для сохранения")
            return
        
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/report_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                r = self.last_result
                f.write("=" * 50 + "\nОТЧЕТ ПО РАСЧЕТУ ГЕОМЕТРИЧЕСКОГО ТЕЛА\n" + "=" * 50 + "\n\n")
                f.write(f"Дата и время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Фигура: {self.current_shape}\nМатериал: {r['material']}\n\n")
                f.write("РЕЗУЛЬТАТЫ РАСЧЕТА:\n" + "-" * 30 + "\n")
                f.write(f"Объем: {r['volume_cm3']} см³ ({r['volume_m3']} м³)\n")
                f.write(f"Площадь поверхности: {r['surface_area_cm2']} см² ({r['surface_area_m2']} м²)\n")
                f.write(f"Масса: {r['mass_g']} г ({r['mass_kg']} кг)\n")
                f.write("=" * 50 + "\n")
            
            self.show_info("Успех", f"Отчет сохранен в файл:\n{filename}")
        except Exception as e:
            self.show_error("Ошибка", f"Не удалось сохранить отчет: {str(e)}")
    
    def show_error(self, title, message):
        Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.3)).open()
    
    def show_info(self, title, message):
        Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.3)).open()

if __name__ == '__main__':
    GeometryApp().run()