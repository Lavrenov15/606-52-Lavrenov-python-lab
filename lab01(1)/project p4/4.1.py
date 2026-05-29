import functools
from datetime import datetime

def logger_decorator(func):
    """Декоратор для логирования вызовов функции"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_name = func.__name__
        
        # Логируем вызов
        print(f"[{timestamp}] ВЫЗОВ: {func_name}(args={args}, kwargs={kwargs})")
        
        # Вызываем функцию
        result = func(*args, **kwargs)
        
        # Логируем результат
        print(f"[{timestamp}] РЕЗУЛЬТАТ: {func_name} -> {repr(result)}")
        
        return result
    return wrapper


@logger_decorator
def file_reader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    index = -1
    
    def get_next_line():
        nonlocal index
        index += 1
        if index < len(lines):
            return lines[index].rstrip('\n')
        else:
            return None
    
    return get_next_line


w = file_reader('пупс.txt')
line = w()
while line is not None:
    print(f"Прочитано: {line}")
    line = w()