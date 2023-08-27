# Get two strings
txt1 = input('Enter a string to compare: ')
txt2 = input('Enter the anagram string to compare: ')


def compare_string(str1, str2):
    # sort both strings and compare
    if sorted(str1) == sorted(str2):
        print(f'"{str2}" is an anagram of "{str1}"')
    else:
        print(f'"{str2}" is not an anagram of "{str1}"')


# call the function
compare_string(txt1, txt2)