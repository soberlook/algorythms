# Посылка 35050896

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


if __name__ == '__main__':
    list_length = int(input())
    search_value = int(input())
    broken_circle_array = list(map(int, input().split()))
    print(broken_binary_search(broken_circle_array, list_length,
                               search_value))
