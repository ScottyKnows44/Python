def reverse_sentence(string):
    ##Splits the string into an array, reverses the array, then joins the array back together 
    return ''.join(string.split()[::-1])


print(reverse_sentence("Hello, World!"))

