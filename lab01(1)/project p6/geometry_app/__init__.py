# geometry_app/__init__.py
"""Пакет для расчета геометрических тел"""

from .shapes import Parallelepiped, Tetrahedron, Sphere
from .materials import MATERIALS, get_material, get_material_names
from .calculations import calculate_shape

__version__ = "1.0.0"
__all__ = [
    'Parallelepiped',
    'Tetrahedron', 
    'Sphere',
    'MATERIALS',
    'get_material',
    'get_material_names',
    'calculate_shape'
]