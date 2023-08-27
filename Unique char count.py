# Getting the input string
str1 = input('Enter a string to find unique characters: ')


def find_unique_char(string):
    comp = []
    # Iterating the string into characters in lower case
    for i in string.lower():
        # If character is not in the list
        # Specific character will be appended to the list
        if i not in comp:
            comp.append(i)
    # Also those specific characters will be counted
    return len(comp)


# Saving the count of specific character and printed
count = find_unique_char(str1)
print('Unique Character count: ', count)