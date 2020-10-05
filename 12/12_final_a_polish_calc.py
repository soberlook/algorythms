# Посылка 34663083

OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) == 0:
            return None
        return self.__items.pop()


def polish_calc(input_list):
    stack = Stack()
    for element in input_list:
        if element in OPERATIONS:
            operand1, operand2 = stack.pop(), stack.pop()
            operation = OPERATIONS[element]
            res = operation(operand2, operand1)
            stack.push(res)
        else:
            stack.push(int(element))
    return stack.pop()


if __name__ == '__main__':
    polish_s = list(input().split())
    print(polish_calc(polish_s))
