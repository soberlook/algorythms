def solution(node):
    print(node)
    while node.next_item:
        node = node.next_item
        print(node)