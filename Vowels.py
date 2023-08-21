String1 = 'Guvi Geeks Network Private Limited'
list1 = ['A', 'E', 'I', 'O', 'U']
No_of_Vowels, a, e, i, o, u = 0, 0, 0, 0, 0, 0
for individual_char1 in String1:
    individual_char1 = individual_char1.upper()
    for individual_char2 in list1:
        if individual_char1 == individual_char2:
            No_of_Vowels += 1
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
print(f'No of A = {a}')
print(f'No of E = {e}')
print(f'No of I = {i}')
print(f'No of O = {o}')
print(f'No of U = {u}')
print(f'Total Number of Vowels = {No_of_Vowels}')