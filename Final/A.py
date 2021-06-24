s = input().split()
a = int(s[1])
n = []

if(a > 9999):
    a = 10000

for i in range(999, a):
    a = 3
    while i >= a:
        a *= 3
        if(i == a):
            n.append(i)

n.reverse()

for i in n:
    print(i, end=" ")