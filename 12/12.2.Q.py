# Задача Q Дек
# Гоша решил реализовать структуру данных Дек, максимальный размер которого определяется заданным числом.
# Методы push_back, push_front, pop_front, pop_back работали корректно.
# Но, если в деке было много элементов, программа работала очень долго.
# Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

# Формат ввода
# В первой строке записано количество команд n - целое число, не превосходящее 5000.
# Во второй строке записано число m - максимальный размер дека.
# Он не превосходит 1000. В следующих n строках записана одна из команд: 
# push_back value
# push_front value
# pop_front
# pop_back
# value - целое число, по модулю не превосходящее 1000.

# Формат вывода
# При вызове команд pop_front и pop_back нужно вывести возвращаемое значение.
# Если они вызываются для пустого дека — напечатайте 'error'.
# Если команда push_back или push_front вызывается для дека,
# размер которого равен максимально возможному, тоже нужно вывести 'error'.


class Deque:
    def __init__(self, m):
        self.items = []
        self.max = m
        self.size = 0
    
    def is_empty(self):
        return self.items == []  
    
    def push_back(self, value):
        if self.size != self.max:
            self.items.append(value)
            self.size += 1
        else:
            print('error')
    
    def push_front(self, value):
        if self.size != self.max:
            self.items.insert(0, value)
            self.size += 1
        else:
            print('error')
    
    def pop_front(self):
        if self.is_empty():
            return 'error'
        else:
            self.size -= 1
            return self.items.pop(0)
    
    def pop_back(self):
        if self.is_empty():
            return 'error'
        else:
            self.size -= 1
            return self.items.pop()
    
    
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    my_deque = Deque(m)
    for i in range(n):
        command = input().split()
        if command[0] == 'push_back':
            my_deque.push_back(int(command[1]))
        elif command[0] == 'push_front':
            my_deque.push_front(int(command[1]))
        elif command[0] == 'pop_front':
            print(my_deque.pop_front())
        elif command[0] == 'pop_back':
            print(my_deque.pop_back())