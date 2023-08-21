list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 0
for i in range(6):
    for j in range(i+1):
        print(list_of_numbers[n], end=' ')
        n += 1
        if n > 19:
            break
    print('\n')