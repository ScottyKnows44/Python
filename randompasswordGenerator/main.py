import random
from collections import Counter
from Person import Person

# Set params for password
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*().,/?{}[]"
length = 20
string = lower + upper + numbers + symbols


def check_if_unique(password_string):
    list = Counter(password_string)
    print({list[i] for i in list if list[i] == 1})


# generate password
password = "".join(random.sample(string, length))
person = Person("Scott", "")

check_if_unique(password)

#print(person.get_password())
