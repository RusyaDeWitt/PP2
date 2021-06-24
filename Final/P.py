a = int(input())
c = 0

for i in range(a):
    for j in range(c, a):
        if(j > a):
            break
        print(j, end=" ")
    print(" ")
    c += 1
    a += 1
