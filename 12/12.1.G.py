# Вася вернулся домой под вечер и вспомнил, что ещё не сделал домашнее
# задание по русскому языку. Чтобы понять разницу между анаграммой и
# палиндромом, Вася снова обратился к Алле. Она объяснила брату, что два
# слова — анаграммы, если одно можно получить из другого перестановкой букв.
# А палиндром — это слово или фраза, которая читается одинаково, если читать
# слева направо и справа налево. Теперь Васе интересно: как закодить
# функцию, определяющую, анаграммы слова или нет. Помогите ему. Формат ввода
#
# Два слова - каждое на отдельной строке.
# Слова состоят из строчных букв латинского и русского алфавитов.
# Формат вывода
#
# Слово True, если слова являются анаграммами друг друга, слово False - если
# не являются.

string1 = input()
string2 = input()

string2 = sorted(string2)
string1 = sorted(string1)

if string1 == string2:
    print('True')
else:
    print('False')



#
#
# def ana(str1, str2):
#     if len(str2) != len(str1):
#         return False
#
#     same_symbols = []
#
#     for symbol in str1:
#         if symbol not in str2:
#             return False
#         else:same_symbols.append(symbol)
#
#     for symbol in same_symbols:
#         if str1.count(symbol) != str2.count(symbol):
#             return False
#     return True
#
#
# print(ana(string1, string2))
