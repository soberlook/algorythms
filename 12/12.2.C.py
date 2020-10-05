# На вход подается строка. Нужно определить длину наибольшей подстроки,
# которая не содержит повторяющиеся символы. Формат ввода
#
# Одна строка, состоящая из латинских букв. Длина строки не превосходит 10000.
# Формат вывода
#
# Одно число - ответ на задачу.
NO_OF_ASCII_CODES = 256


def longest_unique_substring(input_string):
    last_index = [-1] * NO_OF_ASCII_CODES
    input_string_length = len(input_string)
    max_substring_length = 0
    starting_index_of_current_substring = 0

    for current_symbol_index in range(0, input_string_length):
        symbol_ascii_code = ord(input_string[current_symbol_index])
        symbol_last_index_from_array = last_index[symbol_ascii_code]
        last_index[symbol_ascii_code] = current_symbol_index

        starting_index_of_current_substring = max(
            starting_index_of_current_substring,
            symbol_last_index_from_array + 1
        )
        current_substring_length = (current_symbol_index -
                                    starting_index_of_current_substring + 1)

        max_substring_length = max(max_substring_length,
                                   current_substring_length)

    return max_substring_length


string = input()

print(longest_unique_substring(string))
