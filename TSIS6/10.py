def even(l):
    e = []
    for i in range(len(l)):
        if(int(l[i]) % 2 == 0):
            e.append(l[i])
    return e

s = input().split()
print(even(s))