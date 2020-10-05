def is_palindrome(input_str):
    for i in range(0, int(len(input_str) / 2)):
        if input_str[i] != input_str[len(input_str) - i - 1]:
            return False
    return True


string1 = input()

string1 = string1.lower()
string1 = ''.join(x for x in string1 if x.isalpha())

print(is_palindrome(string1))
