# Задача M Очередь
# Перед Тимофеем стоит задача написать несколько реализаций собственной очереди,
# так как доступные на рынке варианты для проекта не подходят.
# Требования к первой вот такие: класс должен называться MyQueue(),
# поддерживать операции добавления, удаления, получения элемента, определение текущего размера, и метод,
# показывающий, пуста ли очередь или нет. Реализована структура данных должна быть на основе массива.

# Формат ввода
# В первой строке записано одно число - количество команд, оно не превосходит 5000.
# Далее идут команды по одной в строке. Команды могут быть следующих видов:
# push x - добавить число x в очередь
# pop - удалить число из очереди и напечатать его
# peek - напечатать первое число в очереди
# size - вернуть размер очереди

# Формат вывода
# Для каждой команды size, peek и pop напечатайте результат её выполнения.
# Если очередь пуста, для команды peek напечатайте None.
# Если происходит удаление из пустой очереди — напечатайте None.

class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)] 
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def push(self, element):
        if self.size != self.max_n:
            self.queue[self.tail] = element
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
    
    def is_empty(self):
        return self.size == 0
    
    def pop(self):
        if self.is_empty():
            return None
        element = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return element
        
    def peek(self):
        return self.queue[self.head]
    
    def get_size(self):
        return self.size
    
    
if __name__ == '__main__':
    n = int(input())
    my_queue = MyQueue(n)
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