str1 = input('Enter a string to find unique characters: ')


def find_unique_char(string):
    comp = []
    num = 0
    for i in string.lower():
        if i not in comp:
            num += 1
            comp.append(i)
    return num


count = find_unique_char(str1)
print('Unique Character count: ', count)