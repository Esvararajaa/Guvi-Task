# Getting the input string
text = input('Enter a string: ')


def is_palindrome(s):
    # Reverse the given string
    rev = ''.join(reversed(s))
    # Compare the given string with reversed string
    if s == rev:
        return True


# Call the function with input string
result = is_palindrome(text)
if result:
    print('True')
else:
    print('False')
