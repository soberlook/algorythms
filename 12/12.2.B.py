# Формат ввода
#
# В первой строке задано число n - количество строк матрицы. Во второй
# строке - m - число столбцов, m и n не превосходит 1000. В следующих n
# строках задана матрица. Числа в матрице по модулю не превосходят 1000.
# Формат вывода
#
# Напечатайте транспонированную матрицу в том же формате.


rows = int(input())
columns = int(input())

matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

transposed = [
    [matrix[j][i] for j in range(rows)]
    for i in range(columns)
]

for row in transposed:
    print(*row)
