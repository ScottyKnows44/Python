array = ["listen", "silent", "hello", "world", "python", "typhon"]


def group_anagrams(array):
    anagram_groups = {}

    for x in array:

        sorted_word = ''.join(sorted(x))

        # if in list add to list
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(x)
        else:
            anagram_groups[sorted_word] = [x]

        # Extract the values (lists of anagrams) from the dictionary
    print(anagram_groups)


group_anagrams(array)
