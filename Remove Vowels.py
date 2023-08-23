def remove_vowels(string1):
    vowels_chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    # iterate the string
    for i in string1:
        # compare each character with vowels list
        if i not in vowels_chars:
            #concatenate non vowels characters
            result = result + i
    print("String without vowels: ", result)


str_var = input("Enter the string to remove vowels: ")
remove_vowels(str_var)
