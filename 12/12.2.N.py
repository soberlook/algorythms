# Задача N Ограниченная очередь
# Далее Тимофею нужно написать класс MyQueueSized(), который принимает параметр max_size,
# означающий максимально допустимое количество элементов в очереди.

# Формат ввода
# В первой строке записано одно число - количество команд, оно не превосходит 5000.
# Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
# Далее идут команды по одной на строке. Команды могут быть следующих видов:
# push x - добавить число x в очередь
# pop - удалить число из очереди и вывести на печать
# peek - напечатать первое число в очереди
# size - вернуть размер очереди
# При превышении допустимого размера очереди нужно вывести "error".
# При вызове операции pop для пустой очереди нужно вернуть None.

# Формат вывода
# Напечатайте результаты выполнения нужных команд, по одному на строке.


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None for _ in range(max_size)] 
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def push(self, element):
        if self.size != self.max_size:
            self.queue[self.tail] = element
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')
    
    def is_empty(self):
        return self.size == 0
    
    def pop(self):
        if self.is_empty():
            return None
        element = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return element
        
    def peek(self):
        return self.queue[self.head]
    
    def get_size(self):
        return self.size
    
    
if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    my_queue = MyQueueSized(max_size)
    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            my_queue.push(int(command[1]))
        elif command[0] == 'peek':
            print(my_queue.peek())
        elif command[0] == 'pop':
            print(my_queue.pop())
        elif command[0] == 'size':
            print(my_queue.get_size())
