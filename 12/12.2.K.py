# Реализуйте класс StackSet, который хранит только уникальные элементы. При
# этом операция добавления элемента в стек должна выполняться за O(1).
# Формат ввода
#
# В первой строке записано одно число - количество команд. Далее идут
# команды по одной на строке. Команды могут быть следующих видов: push x -
# добавить число x в стек pop - удалить число с вершины стека peek -
# напечатать число с вершины стека (без удаления) size - узнать размер стека
# Если стек пуст при вызове команд pop и peak нужно вывести на печать error.


class StackSet:
    def __init__(self):
        self.items = []
        self.seen = set()

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if self.is_empty() or item not in self.seen:
            self.items.append(item)
            self.seen.add(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.items.pop()
        return None

    def peek(self):
        if self.is_empty():
            return 'error'
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = StackSet()
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'peek':
            print(stack.peek())
        elif command[0] == 'pop':
            if stack.pop() is not None:
                print(stack.pop())
        elif command[0] == 'size':
            print(stack.size())

