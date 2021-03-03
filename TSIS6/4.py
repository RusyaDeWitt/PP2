def reverse(s):
    d = ""
    i = len(s)
    while i > 0:
        d += s[i-1]
        i -= 1

    return d

s = input()
print(reverse(s))