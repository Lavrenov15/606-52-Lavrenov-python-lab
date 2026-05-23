# geometry_app/materials.py

class Material:
    """Класс материала"""
    def __init__(self, name, density):
        self.name = name
        self.density = density  # плотность г/см³
    
    def calculate_mass(self, volume_cm3):
        """Расчет массы по объему"""
        return volume_cm3 * self.density

# Справочник материалов
MATERIALS = {
    "Алюминий": Material("Алюминий", 2.70),
    "Сталь": Material("Сталь", 7.85),
    "Медь": Material("Медь", 8.96),
    "Дерево (сосна)": Material("Дерево (сосна)", 0.52),
    "Пластик (ПЭТ)": Material("Пластик (ПЭТ)", 1.38),
    "Золото": Material("Золото", 19.30),
    "Серебро": Material("Серебро", 10.49),
    "Титан": Material("Титан", 4.51)
}

def get_material_names():
    """Получить список названий материалов"""
    return list(MATERIALS.keys())

def get_material(name):
    """Получить материал по названию"""
    return MATERIALS.get(name)