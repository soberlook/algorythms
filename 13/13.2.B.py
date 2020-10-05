# B. Фибоначчи с памятью

# Функция из прошлого задания работала слишком долго.
# Нужно модифицировать ее таким образом, чтобы одни и те же значения повторно не вычислялись.

# Формат ввода
# На вход подается число n.

# Формат вывода
# Напечатайте n-ное число Фибоначчи.

FIB_DICT = {0: 1, 1: 1}

def fibonacci_number(n):
    if n in FIB_DICT:
        return FIB_DICT[n]
    FIB_DICT[n] = fibonacci_number(n-1) + fibonacci_number(n-2)
    return FIB_DICT[n]

with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.read())
    print(fibonacci_number(n))
    