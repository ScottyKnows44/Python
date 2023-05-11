def is_anagram(string1, string2):
    #Clean string and get rid of spaces and capital letters
    str1 = string1.replace(" ", "").lower()
    str2 = string2.replace(" ", "").lower()

    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)

    return str1_sorted == str2_sorted


print(is_anagram("eleven plus two", "twelve plus one"))

