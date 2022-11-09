import random

# Set params for password
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*().,/?{}[]"
length = 20
string = lower + upper + numbers + symbols

#Print password
print("Password: " + "".join(random.sample(string, length)))
