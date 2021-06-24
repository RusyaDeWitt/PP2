s = input().split()
n = set()


for i in s:
    a = 2
    i = int(i)
    if(i == 1):
        n.add(1)
    if(i == 2):
        n.add(2)
    while i >= a:
        a *= 2
        if(i == a):
            n.add(i)

for i in sorted(n):
    print(i, end=" ")