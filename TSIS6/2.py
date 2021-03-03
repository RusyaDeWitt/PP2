def sumList(l):
    sum = 0
    for i in l:
        sum += int(i)

    return sum

l = input().split()
print("Sum:", sumList(l))
