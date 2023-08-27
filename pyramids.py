n = 1
a = 5
# Rows to use
for i in range(a):
    # Inverted right angle triangle with 'space'
    for j in range(i, a):
        print(' ', end=' ')
    # Mirrored right angle triangle with 'consequent numbers'
    for j in range(i):
        # tried to improvise the pyramid
        if n <= 9:
            print(f'0{n}', end='')
        else:
            print(f'{n}', end='')
        n += 1
    # Restricting the number value till 20
    if n > 19:
        break
    # Right-angled triangle with 'consequent numbers'
    for j in range(i+1):
        # tried to improvise the pyramid
        if n <= 9:
            print(f'0{n}', end='')
        else:
            print(f'{n}', end='')
        n += 1
    print()