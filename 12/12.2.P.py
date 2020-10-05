# Задача P Списочная очередь
# Любимый вариант очереди Тимофея - очередь, написанная с использованием связного списка.
# Помогите ему с реализацией. Очередь должна поддерживать методы get, put, size.

# Формат ввода
# В первой строке записано количество команд n - целое число, не превосходящее 1000.
# В каждой из следующих n строк записана команда: get, put, или size.

# Формат вывода
# При вызове метода get напечатайте возвращаемое значение.
# Если метод get вызывается у пустой очереди, нужно напечатать 'error'.
# При вызове метода size - вывести размер очереди.


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return self.value
    
    

class ListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self):
        if self.head == None:
            return 'error'
        else:
            tmp = self.head
            self.head = self.head.next
            self.size -= 1
            return tmp

    def put(self, value):
        self.size += 1
        if self.head == None:
            self.tail = self.head = Node(value, None)
        else:
            self.tail.next = self.tail = Node(value, None)

    def get_size(self):
        return self.size
    

if __name__ == '__main__':
    n = int(input())
    list_queue = ListQueue()
    for i in range(n):
        command = input().split()
        if command[0] == 'put':
            list_queue.put(str(command[1]))
        elif command[0] == 'get':
            print(list_queue.get())
        elif command[0] == 'size':
            print(list_queue.get_size())