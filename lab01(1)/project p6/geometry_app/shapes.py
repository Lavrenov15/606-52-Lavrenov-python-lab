# geometry_app/shapes.py
import math

class Parallelepiped:
    """Класс параллелепипеда"""
    def __init__(self, length, width, height):
        self.length = length  # длина
        self.width = width    # ширина
        self.height = height  # высота
    
    def volume(self):
        """Объем параллелепипеда"""
        return self.length * self.width * self.height
    
    def surface_area(self):
        """Площадь поверхности параллелепипеда"""
        return 2 * (self.length * self.width + 
                   self.length * self.height + 
                   self.width * self.height)

class Tetrahedron:
    """Класс правильного тетраэдра"""
    def __init__(self, edge):
        self.edge = edge  # длина ребра
    
    def volume(self):
        """Объем правильного тетраэдра"""
        return (self.edge ** 3) / (6 * math.sqrt(2))
    
    def surface_area(self):
        """Площадь поверхности правильного тетраэдра"""
        return math.sqrt(3) * (self.edge ** 2)

class Sphere:
    """Класс шара"""
    def __init__(self, radius):
        self.radius = radius  # радиус
    
    def volume(self):
        """Объем шара"""
        return (4/3) * math.pi * (self.radius ** 3)
    
    def surface_area(self):
        """Площадь поверхности шара"""
        return 4 * math.pi * (self.radius ** 2)