# Посылка 34663239

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(head):
    first_racer = head
    second_racer = head
    while second_racer is not None and second_racer.next is not None:
        first_racer = first_racer.next
        second_racer = second_racer.next.next
        if first_racer is second_racer:
            return True
    return False

