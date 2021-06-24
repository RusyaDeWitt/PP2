s = input().split()
d = { }


for i in s:
    tmp = 0
    for j in s:
        if(j == i):
            tmp += 1
    d[i] = tmp

for x, y in sorted(d.items()):
    print(x, y)