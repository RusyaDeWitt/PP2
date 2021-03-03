def upper(s):
    upper = 0
    for i in range(len(s)):
        if(s[i].isupper()):
            upper += 1

    return upper


s = input()
s = s.replace(' ', '')

d = int(upper(s))

print("Upper:", d)
print("Lower:", len(s)-d)