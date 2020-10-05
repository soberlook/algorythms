# Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
# Если вы с ней еще не сталкивались, то наверняка столкнётесь — она довольно
# популярная. Дана скобочная последовательность. Нужно определить,
# правильная ли она. Будем придерживаться такого определения: - пустая
# строка — правильная скобочная последовательность; - правильная скобочная
# последовательность, взятая в скобки одного типа, — правильная скобочная
# последовательность; - правильная скобочная последовательность с
# приписанной слева или справа правильной скобочной последовательностью —
# тоже правильная. На вход подается последовательность из скобок трёх видов:
# [], (), {}. Напишите функцию is_correct_bracket_seq, которая принимает на
# вход скобочную последовательность и возвращает True,
# если последовательность правильная, иначе False.
#


class Stack(list):

    def is_empty(self):
        return self == []

    def push(self, item):
        self.append(item)

    def peek(self):
        if self.is_empty():
            return None
        return self[len(self) - 1]

    def size(self):
        return len(self)


def is_correct_bracket_seq(string):
    OPENING_BRACKETS = ('(', '[', '{')
    stack = Stack()

    for symbol in string:
        if stack.peek() == '{' and symbol == '}':
            stack.pop()
        elif stack.peek() == '(' and symbol == ')':
            stack.pop()
        elif stack.peek() == '[' and symbol == ']':
            stack.pop()
        elif symbol in OPENING_BRACKETS:
        #else:
            stack.push(symbol)
    return stack.is_empty()


input_string = input()
print(is_correct_bracket_seq(input_string))
