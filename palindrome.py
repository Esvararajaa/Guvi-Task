text = input('Enter a string: ')


def is_palindrome(s):
    rev = ''.join(reversed(s))
    if s == rev:
        return True
    else:
        return False


result = is_palindrome(text)
if result:
    print('True')
else:
    print('False')
