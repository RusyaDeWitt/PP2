a = list(map(int, input().strip().split()))

for i in range(len(a)):
    if (i % 2 == 0):
        print(a[i], end=" ")
