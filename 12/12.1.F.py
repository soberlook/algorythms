# Алла писала код, добавляющий запись в новую таблицу базы данных. И вдруг
# получила ошибку duplicate foreign key constraint. В тот же момент её
# отвлекла Рита. Алла случайно закрыла окно терминала с информацией о том,
# какое именно значение стало причиной ошибки. Зато у неё сохранился список
# id, использованных при запросе. Помогите ей выяснить, какой id стал
# причиной ошибки.
#
# Дан массив чисел, состоящий  из n целых чисел. Одно число
# встречается более одного раза. Нужно определить это число. Формат ввода
#
# В первой строке записано число n, которое не превосходит 1000. В следующей
# строке через пробел записаны n целых чисел, каждое из которых также не
# превосходит 10000. Формат вывода
#
# Выведите одно число.
# Пример 1
#
# Ввод
# 5
# 3 1 3 4 2
#
# Вывод
# 3
# Пример 2
#
# Ввод
# 3
# 2 8 8
# Вывод
# 8
#

n = int(input())
ids = list(map(int, input().split()))



uniques = []
res = 0

for el in ids:
    if el in uniques:
        res = el
    uniques.append(el)

print(res)


