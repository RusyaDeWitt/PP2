def perfect(n):
    l = []
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            l.append(i)

    for i in l:
        sum += i

    if(sum == n):
        return "Yes"
    if(sum != n):
        return "No"

n = int(input())
print(perfect(n))