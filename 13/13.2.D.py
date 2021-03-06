# D. Последняя цифра

# У одного жителя деревни Упыревка очень старый компьютер.
# На экран он может выводить только одну цифру, причем последнюю из тех,
# что выводится в стандартный поток вывода. Помогите жителю Упыревки понять,
# что должно быть выведено на экран, когда он запустит программу для вычисления n - ого числа Фибоначчи.

# Формат ввода
# На вход подается n - целое число в диапазоне от 0 до 10000

# Формат вывода
# Нужно вывести одну цифру, последнюю в числе, равному n - ому числу Фибоначчи

# Примечания
# В решении не должно вычисляться само число Фибоначчи. Диапазон подаваемых на вход данных достаточно большой.

def get_fibonacci_last_digit(n):
    if n in (0, 1):
        return 1
    first_digit = 0
    second_digit = 1
    for __ in range(n):
        tmp = (first_digit + second_digit) % 10
        first_digit = second_digit
        second_digit = tmp
    return second_digit

with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.read())
    print(get_fibonacci_last_digit(n))
    