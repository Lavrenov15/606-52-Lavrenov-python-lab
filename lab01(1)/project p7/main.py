import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any, Optional
import os

from geometry_app.calculations import calculate_shape
from geometry_app.materials import get_material_names


class Shape(ABC):
    """Абстрактный базовый класс для геометрических фигур"""
    
    def __init__(self, name: str):
        self._name = name
        self._dimensions: Dict[str, float] = {}
        self._material: Optional[str] = None
        
    @property
    def name(self) -> str:
        """Managed attribute для названия фигуры"""
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Название фигуры должно быть непустой строкой")
        self._name = value
    
    @property
    def dimensions(self) -> Dict[str, float]:
        """Managed attribute для размеров фигуры"""
        return self._dimensions.copy()
    
    @dimensions.setter
    def dimensions(self, values: Dict[str, float]):
        if not values:
            raise ValueError("Размеры не могут быть пустыми")
        for key, val in values.items():
            if val <= 0:
                raise ValueError(f"Размер {key} должен быть положительным числом")
        self._dimensions = values
    
    @property
    def material(self) -> Optional[str]:
        return self._material
    
    @material.setter
    def material(self, value: str):
        if value and isinstance(value, str):
            self._material = value
    
    @abstractmethod
    def get_shape_type(self) -> str:
        """Абстрактный метод для получения типа фигуры"""
        pass
    
    @abstractmethod
    def get_input_fields(self) -> list:
        """Абстрактный метод для получения полей ввода"""
        pass
    
    def __str__(self) -> str:
        """Dunder-метод для строкового представления"""
        return f"{self._name} (материал: {self._material or 'не выбран'})"
    
    def __eq__(self, other) -> bool:
        """Dunder-метод для сравнения фигур"""
        if not isinstance(other, Shape):
            return False
        return self._name == other._name and self._dimensions == other._dimensions
    
    def __repr__(self) -> str:
        return f"Shape(name='{self._name}')"


class Parallelepiped(Shape):
    """Класс для параллелепипеда"""
    
    def __init__(self):
        super().__init__("Параллелепипед")
        self._length: float = 0.0
        self._width: float = 0.0
        self._height: float = 0.0
    
    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, value: float):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._length = value
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._width = value
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: float):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._height = value
    
    def get_shape_type(self) -> str:
        return "parallelepiped"
    
    def get_input_fields(self) -> list:
        return [("Длина (см):", "length"), ("Ширина (см):", "width"), ("Высота (см):", "height")]
    
    def __str__(self) -> str:
        return f"{super().__str__()} (длина={self._length}, ширина={self._width}, высота={self._height})"
    
    def __repr__(self) -> str:
        return f"Parallelepiped(length={self._length}, width={self._width}, height={self._height})"


class Tetrahedron(Shape):
    """Класс для тетраэдра"""
    
    def __init__(self):
        super().__init__("Тетраэдр")
        self._edge: float = 0.0
    
    @property
    def edge(self) -> float:
        return self._edge
    
    @edge.setter
    def edge(self, value: float):
        if value <= 0:
            raise ValueError("Длина ребра должна быть положительной")
        self._edge = value
    
    def get_shape_type(self) -> str:
        return "tetrahedron"
    
    def get_input_fields(self) -> list:
        return [("Длина ребра (см):", "edge")]
    
    def __str__(self) -> str:
        return f"{super().__str__()} (ребро={self._edge})"
    
    def __repr__(self) -> str:
        return f"Tetrahedron(edge={self._edge})"


class Sphere(Shape):
    """Класс для шара"""
    
    def __init__(self):
        super().__init__("Шар")
        self._radius: float = 0.0
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = value
    
    def get_shape_type(self) -> str:
        return "sphere"
    
    def get_input_fields(self) -> list:
        return [("Радиус (см):", "radius")]
    
    def __str__(self) -> str:
        return f"{super().__str__()} (радиус={self._radius})"
    
    def __repr__(self) -> str:
        return f"Sphere(radius={self._radius})"


class ShapeFactory:
    """Фабрика для создания фигур"""
    
    @staticmethod
    def create_shape(shape_name: str) -> Shape:
        shapes = {
            "Параллелепипед": Parallelepiped,
            "Тетраэдр": Tetrahedron,
            "Шар": Sphere
        }
        
        shape_class = shapes.get(shape_name)
        if not shape_class:
            raise ValueError(f"Неизвестный тип фигуры: {shape_name}")
        
        return shape_class()
    
    def __str__(self) -> str:
        return "Фабрика создания геометрических фигур"
    
    def __repr__(self) -> str:
        return "ShapeFactory()"


class GeometryApp:
    """Главный класс приложения"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор геометрических тел")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        self.current_shape: Optional[Shape] = None
        self.last_result: Optional[Dict[str, Any]] = None
        self.input_fields: Dict[str, tk.Entry] = {}
        
        self.init_ui()
    
    def init_ui(self):
        """Инициализация интерфейса"""
        # Заголовок
        title_label = tk.Label(self.root, text="Калькулятор геометрических тел", 
                               font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        # Фрейм для выбора фигуры
        shape_frame = tk.Frame(self.root)
        shape_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(shape_frame, text="Выберите фигуру:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        self.shape_var = tk.StringVar(value="Параллелепипед")
        self.shape_combo = ttk.Combobox(shape_frame, textvariable=self.shape_var, 
                                        values=["Параллелепипед", "Тетраэдр", "Шар"],
                                        state="readonly", width=20)
        self.shape_combo.pack(side=tk.LEFT, padx=5)
        self.shape_combo.bind("<<ComboboxSelected>>", self.on_shape_change)
        
        # Фрейм для полей ввода
        self.input_frame = tk.LabelFrame(self.root, text="Параметры фигуры", padx=10, pady=10)
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Фрейм для выбора материала
        material_frame = tk.Frame(self.root)
        material_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(material_frame, text="Выберите материал:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        self.material_var = tk.StringVar(value="Алюминий")
        self.material_combo = ttk.Combobox(material_frame, textvariable=self.material_var,
                                           values=get_material_names(),
                                           state="readonly", width=20)
        self.material_combo.pack(side=tk.LEFT, padx=5)
        
        # Фрейм для кнопок
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.calc_button = tk.Button(button_frame, text="Рассчитать", 
                                     command=self.calculate, bg="#4CAF50", fg="white",
                                     font=("Arial", 10, "bold"), padx=20, pady=5)
        self.calc_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = tk.Button(button_frame, text="Сохранить отчет", 
                                     command=self.save_report, bg="#2196F3", fg="white",
                                     font=("Arial", 10, "bold"), padx=20, pady=5,
                                     state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        # Результаты
        result_label = tk.Label(self.root, text="Результаты:", font=("Arial", 12, "bold"))
        result_label.pack(anchor=tk.W, padx=10, pady=5)
        
        self.result_text = scrolledtext.ScrolledText(self.root, height=15, width=90,
                                                      font=("Courier", 10))
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.result_text.insert(tk.END, "Нажмите 'Рассчитать' для получения результатов")
        self.result_text.config(state=tk.DISABLED)
        
        # Инициализация полей ввода
        self.update_input_fields("Параллелепипед")
    
    def on_shape_change(self, event=None):
        """Обработчик изменения фигуры"""
        shape_name = self.shape_var.get()
        self.update_input_fields(shape_name)
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Нажмите 'Рассчитать' для получения результатов")
        self.result_text.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)
        self.last_result = None
    
    def update_input_fields(self, shape_name: str):
        """Обновление полей ввода в зависимости от фигуры"""
        # Очищаем существующие поля
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        self.input_fields.clear()
        
        # Создаем новую фигуру
        self.current_shape = ShapeFactory.create_shape(shape_name)
        
        # Создаем поля ввода
        for i, (label_text, attr_name) in enumerate(self.current_shape.get_input_fields()):
            tk.Label(self.input_frame, text=label_text, font=("Arial", 10)).grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = tk.Entry(self.input_frame, width=20, font=("Arial", 10))
            entry.insert(0, "10")
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.input_fields[attr_name] = entry
    
    def get_dimensions(self) -> Dict[str, float]:
        """Получение размеров из полей ввода"""
        dimensions = {}
        
        for attr_name, entry in self.input_fields.items():
            try:
                value = float(entry.get())
                if value <= 0:
                    raise ValueError("Размер должен быть положительным числом")
                dimensions[attr_name] = value
            except ValueError as e:
                if str(e) == "Размер должен быть положительным числом":
                    raise
                raise ValueError(f"Некорректное значение для поля {attr_name}. Введите число.")
        
        return dimensions
    
    def calculate(self):
        """Обработчик кнопки расчета"""
        try:
            dimensions = self.get_dimensions()
            material = self.material_var.get()
            
            # Устанавливаем размеры в объект фигуры
            if isinstance(self.current_shape, Parallelepiped):
                self.current_shape.length = dimensions['length']
                self.current_shape.width = dimensions['width']
                self.current_shape.height = dimensions['height']
            elif isinstance(self.current_shape, Tetrahedron):
                self.current_shape.edge = dimensions['edge']
            elif isinstance(self.current_shape, Sphere):
                self.current_shape.radius = dimensions['radius']
            
            self.current_shape.material = material
            
            # Выполняем расчет
            self.last_result = calculate_shape(
                self.current_shape.get_shape_type(),
                dimensions,
                material
            )
            
            self.display_result()
            self.save_button.config(state=tk.NORMAL)
            
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def display_result(self):
        """Отображение результатов"""
        if not self.last_result:
            return
        
        r = self.last_result
        result_text = f"""
Фигура: {self.current_shape.name}
Материал: {r['material']}

Объем:
  • {r['volume_cm3']:.2f} см³
  • {r['volume_m3']:.6f} м³

Площадь поверхности:
  • {r['surface_area_cm2']:.2f} см²
  • {r['surface_area_m2']:.4f} м²

Масса:
  • {r['mass_g']:.2f} г
  • {r['mass_kg']:.3f} кг
"""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)
        self.result_text.config(state=tk.DISABLED)
    
    def save_report(self):
        """Обработчик сохранения отчета"""
        if not self.last_result:
            messagebox.showwarning("Предупреждение", "Нет результатов для сохранения")
            return
        
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/report_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                r = self.last_result
                f.write("=" * 50 + "\nОТЧЕТ ПО РАСЧЕТУ ГЕОМЕТРИЧЕСКОГО ТЕЛА\n" + "=" * 50 + "\n\n")
                f.write(f"Дата и время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Фигура: {self.current_shape.name}\nМатериал: {r['material']}\n\n")
                f.write("РЕЗУЛЬТАТЫ РАСЧЕТА:\n" + "-" * 30 + "\n")
                f.write(f"Объем: {r['volume_cm3']:.2f} см³ ({r['volume_m3']:.6f} м³)\n")
                f.write(f"Площадь поверхности: {r['surface_area_cm2']:.2f} см² ({r['surface_area_m2']:.4f} м²)\n")
                f.write(f"Масса: {r['mass_g']:.2f} г ({r['mass_kg']:.3f} кг)\n")
                f.write("=" * 50 + "\n")
            
            messagebox.showinfo("Успех", f"Отчет сохранен в файл:\n{filename}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить отчет: {str(e)}")
    
    def __str__(self) -> str:
        return f"GeometryApp(title='{self.root.title()}')"
    
    def __repr__(self) -> str:
        return f"GeometryApp(size={self.root.geometry()})"


if __name__ == '__main__':
    root = tk.Tk()
    app = GeometryApp(root)
    root.mainloop()