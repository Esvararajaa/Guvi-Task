str1 = input('Enter a string: ')


def find_word_count(s):
    count = len(s.split())
    return count


result = find_word_count(str1)
print('Total word count: ', result)