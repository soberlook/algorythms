# Васе очень понравилась задача про анаграммы и он придумал к ней
# модификацию. Есть 2 строки s и t, состоящие только из строчных букв.
# Строка t получена перемешиванием букв строки s и добавлением 1 буквы в
# случайную позицию. Нужно найти добавленную букву.


string1 = input()
string2 = input()

string2 = sorted(string2)
string1 = sorted(string1)

longest = 0
res = ''


if len(string1) > len(string2):
    longest = string1
    shortest = string2
else:
    longest = string2
    shortest = string1


for i in range(len(shortest)):
    s1 = longest[i]
    s2 = shortest[i]
    if longest[i] != shortest[i]:
        res = longest[i]
        break

if res == '':
    res = longest[-1]

print(res)