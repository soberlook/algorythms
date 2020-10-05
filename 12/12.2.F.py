def solution(node, number):
    head = node
    if number == 0:
        new_head = head.next_item
        del head
        return new_head
    while number-1:
        node = node.next_item
        number -= 1
    tmp = node.next_item
    node.next_item = tmp.next_item
    del tmp
    return head