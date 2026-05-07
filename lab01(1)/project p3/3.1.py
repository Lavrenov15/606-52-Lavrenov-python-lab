def unpack_recursive(lst):
    result = []
    
    def extract(item):
        if isinstance(item, (list, tuple)):
            for sub_item in item:
                extract(sub_item)
        elif isinstance(item, set):
            for sub_item in item:
                extract(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                extract(key)
                extract(value)
        else:
            result.append(item)
    
    extract(lst)
    return result


def unpack_iterative(lst):
    result = []
    stack = [lst]
    
    while stack:
        current = stack.pop()
        
        if isinstance(current, (list, tuple)):
            for item in reversed(current):
                stack.append(item)
        elif isinstance(current, set):
            for item in current:
                stack.append(item)
        elif isinstance(current, dict):
            for key, value in list(current.items())[::-1]:
                stack.append(value)
                stack.append(key)
        else:
            result.append(current)
    
    return result


# Проверка
test_data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
print("Рекурсивная:", unpack_recursive(test_data))
print("Итеративная:", unpack_iterative(test_data))