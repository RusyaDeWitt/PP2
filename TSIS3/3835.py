a = list(map(int, input().strip().split()))

min = 10**10

for i in range(len(a)):
    if(a[i] > 0):
        if(a[i] < min):
            min = a[i]

print(min)