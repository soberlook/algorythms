# А теперь помогите Васе решить задачу по информатике. Он снова томится дома
# в хорошую погоду. На вход подается строка длиной от 1 до 10000 символов.
# Нужно отсортировать её в порядке частот букв по встречаемости. Заглавные и
# строчные буквы считаются разными. Если частота одинаковая, нужно применить
# вторичную сортировку лексикографически.

res = ''
sym_qty = {}


string1 = input()
string1 = sorted(string1)

uniques = ''.join(set(string1))


for i in range(len(uniques)):
    sym_qty[uniques[i]] = string1.count(uniques[i])


sym_qty = sorted(sym_qty.items(), key=lambda x: (-x[1], x[0]))

for el in sym_qty:
    res = res.ljust(int(el[1]) + len(res), el[0])


print(res)
