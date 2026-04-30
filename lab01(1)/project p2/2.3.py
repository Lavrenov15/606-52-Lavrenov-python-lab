def div(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return True
    return False

count = 0
for x in range(245690, 245756 + 1):
    if x > 1 and not div(x):
        count += 1
        print(count, x)

    