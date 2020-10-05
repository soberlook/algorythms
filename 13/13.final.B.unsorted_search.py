# Посылка 35050896 (для рекурсивного метода)
# Посылка 35189268 (для итеративного метода)

def broken_binary_search(broken_array, length, value):
    broken_point = find_broken_point(broken_array, 0, length - 1)
    if broken_point == -1:
        return binary_search(broken_array, 0, length - 1, value)
    if broken_array[broken_point] == value:
        return broken_point
    if broken_array[0] <= value:
        return binary_search(broken_array, 0, broken_point - 1, value)
    return binary_search(broken_array, broken_point + 1, length - 1, value)


def find_broken_point(broken_array, lower_index, higher_index):
    if higher_index < lower_index:
        return -1
    if higher_index == lower_index:
        return higher_index
    middle = int((higher_index + lower_index) / 2)
    if broken_array[middle + 1] < broken_array[middle]:
        return middle
    if broken_array[lower_index] > broken_array[middle]:
        return find_broken_point(broken_array, lower_index, middle - 1)
    return find_broken_point(broken_array, middle + 1, higher_index)


def binary_search(array, lower_index, higher_index, value):
    if higher_index < lower_index:
        return -1
    middle = int((lower_index + higher_index) / 2)
    if value == array[middle]:
        return middle
    if value > array[middle]:
        return binary_search(array, middle + 1, higher_index, value)
    return binary_search(array, lower_index, middle - 1, value)


def iterative_binary_search(array, value):
    lower_index = 0
    higher_index = len(array) - 1
    middle = 0
    while lower_index <= higher_index:
        middle = int((lower_index + higher_index) / 2)
        if array[middle] < value:
            lower_index = middle + 1
        elif array[middle] > value:
            higher_index = middle - 1
        else:
            return middle
    return -1


def iterative_broken_point(array):
    lower_index = 0
    higher_index = len(array) - 1
    middle = 0

    while lower_index <= higher_index:
        if lower_index == higher_index:
            return higher_index
        middle = (higher_index + lower_index) // 2
        if array[middle + 1] < array[middle]:
            return middle
        if array[lower_index] > array[middle]:
            higher_index = middle - 1
        else:
            lower_index = middle + 1
    return -1


def iterative_broken_search(array, value):
    broken_point = iterative_broken_point(array)
    if broken_point == -1:
        return iterative_binary_search(array, value)
    if array[broken_point] == value:
        return broken_point
    if array[0] <= value:
        return iterative_binary_search(array[0:broken_point - 1], value)
    if iterative_binary_search(array[broken_point + 1:], value) == -1:
        return -1
    else:
        res = iterative_binary_search(array[broken_point + 1:], value)
        return broken_point + 1 + res


if __name__ == '__main__':
    list_length = int(input())
    search_value = int(input())
    broken_circle_array = list(map(int, input().split()))
    # рекурсивный метод:
    # print(broken_binary_search(broken_circle_array, list_length,
    #                            search_value))
    #
    # итеративный метод:
    print(iterative_broken_search(broken_circle_array, search_value))
