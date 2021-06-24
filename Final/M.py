s = input()
d = { }


for i in range(len(s)):
    tmp = 0
    for j in range(len(s)):
        if(s[j] == s[i]):
            tmp += 1
    d[s[i]] = tmp


print(len(d))
for x,y in sorted(d.items()):
    print(x,y)