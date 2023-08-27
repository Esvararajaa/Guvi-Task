# Using the regex
import re
# Getting the input string
str1 = input('Enter a string: ')


# Using the regex (findall) function to count words
def find_word_count(s):
    count = len(re.findall(r'\w+', s))
    return count


# Storing the return value and printing it
result = find_word_count(str1)
print('Total word count: ', result)