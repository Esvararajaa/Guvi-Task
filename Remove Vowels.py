def remove_vowels(string1):
    vowels_chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    for i in string1:
        if i not in vowels_chars:
            result = result + i
    print("String without vowels: ", result)


str_var = input("Enter the string to remove vowels: ")
remove_vowels(str_var)
