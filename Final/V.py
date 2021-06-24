s = input().split()
n = [ ]

a = int(s[0])
b = int(s[1])
c = int(s[2])

for i in range(1,a+1):
    if(a % i == 0 and b % i == 0):
        n.append(i)
n.reverse()
print(n[c-1])