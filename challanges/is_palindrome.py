def is_palindrome(string):
    # iterates through string and joins only the chars and ints together
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


print(is_palindrome("Split a string into 2 in Python"))
