import math

def is_palindrome(string):
    # iterates through string and joins only the chars and ints together
    cleaned_string = ''.join(char.lower() for char in str(string) if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


def is_prime(n):

    #numbers less than two or not prime numbers
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 2):
        if n % i == 0:
            return False
    return True


def is_prime_palindrome(string):
    for i in range(int(string), -1, -1):
        if is_palindrome(i) and is_prime(i):
            return i


print(is_prime_palindrome(1000))