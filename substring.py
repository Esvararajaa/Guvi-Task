str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
new_l, new1 = [], []


# function to find the available substrings for the given string
def substring(test_str):
    new_str = test_str.replace(" ", "")
    res = []
    for i in range(len(new_str)):
        for j in range(i + 1, len(new_str) + 1):
            res.append(new_str[i:j])
    return res


# Compare and find the same substring available
for m in substring(str1):
    for n in substring(str2):
        if m == n:
            new1.append(m)
# Find the length and max among them from new1
for k in new1:
    new_l.append(len(k))
max_len_ss = max(new_l)
# Compare the max len with the common substring length and print the output
for p in new1:
    if max_len_ss == len(p):
        print(f"Longest common substring: {p}")
