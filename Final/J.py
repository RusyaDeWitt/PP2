def prime(x):
    if(x == 1):
        return False
    for i in range(2,x):
        if(x % i == 0):
            return False
    return True


s = input().split()
n = []

for i in range(int(s[0]), int(s[1])):
    if(prime(i) == True):
        n.append(i)

n.reverse()
for i in n:
    print(i, end=" ")