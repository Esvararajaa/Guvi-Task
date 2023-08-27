# Used the string from the question
String1 = 'Guvi Geeks Network Private Limited'
list1 = ['A', 'E', 'I', 'O', 'U']

# Initializing the count of each vowels
No_of_Vowels, a, e, i, o, u = 0, 0, 0, 0, 0, 0
# Iterating the string into characters
for individual_char1 in String1:
    # Saving the character to a upper case
    individual_char1 = individual_char1.upper()

    for individual_char2 in list1:
        # Comparing the characters of the string with vowels
        if individual_char1 == individual_char2:
            # Counting the total number of available vowels in the string
            No_of_Vowels += 1

    # Below counting the individual vowel characters
    if individual_char1 == 'A':
        a += 1
    if individual_char1 == 'E':
        e += 1
    if individual_char1 == 'I':
        i += 1
    if individual_char1 == 'O':
        o += 1
    if individual_char1 == 'U':
        u += 1

# Printing the vowel count using the formatted string
print(f'No of A = {a}')
print(f'No of E = {e}')
print(f'No of I = {i}')
print(f'No of O = {o}')
print(f'No of U = {u}')
print(f'Total Number of Vowels = {No_of_Vowels}')