def unique(l):
    s = set()
    for i in range(len(l)):
        s.add(int(l[i]))
    return  s

l = input().split()
print(unique(l))