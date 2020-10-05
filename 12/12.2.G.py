def solution(node, element):
    
    if node.value == element:
        return 0
    
    node = node.next_item
    n = 1
    while node:
        if node.value == element:
            return n
        node = node.next_item
        n += 1
    
    return -1