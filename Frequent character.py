from collections import Counter
# initializing string
str1 = input("Enter the string: ")


# Finding the frequent character
def get_key(s):
    val = max(Counter(s).values())
    for key, value in Counter(s).items():
        if val == value:
            return key


# printing the specific character
max_char = get_key(str1)
print(f'Max number of character in the string: {max_char}')