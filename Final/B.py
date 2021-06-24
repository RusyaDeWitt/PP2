s = input().split()
n = []


for i in s:
    t = False
    for j in s:
        if(sorted(i) == sorted(j)):
            t = True
    if(t == True):
        n.append(i)

for i in sorted(n):
    print(i)