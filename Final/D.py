s = input().split()
a = set()


for i in s:
    if(i != i[::-1]):
        a.add(i)

for i in sorted(a):
    print(i)