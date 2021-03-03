def factorial(n):
    tot = 1
    for i in range(1, n+1):
        tot *= i

    return tot

n = int(input("Input num: "))
print(factorial(n))
