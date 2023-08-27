# Function to get string
def remove_vowels(string1):
    vowels_chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # Empty string to save the new string
    result = ''
    # Iterating the string into characters
    for i in string1:
        if i not in vowels_chars:
            # If the individual characters are not in the vowel list
            # Then such characters gets appended in the empty string
            result = result + i
    print("String without vowels: ", result)


# Getting string as input
str_var = input("Enter the string to remove vowels: ")
# Call the function by passing the input string
remove_vowels(str_var)
