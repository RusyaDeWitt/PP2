def multiList(l):
    sum = 1
    for i in l:
        sum *= int(i)

    return sum

l = input().split()
print("Multiplication:", multiList(l))
