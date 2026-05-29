# geometry_app/calculations.py
from .shapes import Parallelepiped, Tetrahedron, Sphere
from .materials import get_material

def calculate_shape(shape_type, dimensions, material_name):
    """
    Выполнить расчет для геометрической фигуры
    
    Параметры:
    - shape_type: тип фигуры ('parallelepiped', 'tetrahedron', 'sphere')
    - dimensions: словарь с размерами
    - material_name: название материала
    
    Возвращает: словарь с результатами расчетов
    """
    
    # Создаем фигуру
    if shape_type == 'parallelepiped':
        shape = Parallelepiped(
            dimensions['length'],
            dimensions['width'],
            dimensions['height']
        )
    elif shape_type == 'tetrahedron':
        shape = Tetrahedron(dimensions['edge'])
    elif shape_type == 'sphere':
        shape = Sphere(dimensions['radius'])
    else:
        raise ValueError(f"Неизвестный тип фигуры: {shape_type}")
    
    # Вычисляем объем и площадь
    volume_cm3 = shape.volume()
    surface_area_cm2 = shape.surface_area()
    
    # Получаем материал и вычисляем массу
    material = get_material(material_name)
    if material:
        mass_g = material.calculate_mass(volume_cm3)
        mass_kg = mass_g / 1000
    else:
        mass_g = 0
        mass_kg = 0
    
    # Формируем результат
    result = {
        'volume_cm3': round(volume_cm3, 2),
        'volume_m3': round(volume_cm3 / 1_000_000, 6),
        'surface_area_cm2': round(surface_area_cm2, 2),
        'surface_area_m2': round(surface_area_cm2 / 10_000, 4),
        'mass_g': round(mass_g, 2),
        'mass_kg': round(mass_kg, 3),
        'material': material_name
    }
    
    return result