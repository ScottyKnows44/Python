string = "programming"


def first_non_repeating_char(par):
    array = {}

    for char in par:
        if char in array:
            array[char] += 1
        else:
            array[char] = 1

    for char in array:
        if array[char] == 1:
            print(char)


first_non_repeating_char(string)


