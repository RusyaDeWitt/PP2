s = input().split()
s = set(s)

for i in s:
    a = 2
    while int(i) >= a:
        a *= 2
        if(i == a):
            s.remove(i)

sorted(s)
for i in s:
    print(i, end=" ")