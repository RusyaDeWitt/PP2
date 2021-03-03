def isPrime(n):
    s = 2
    tot = 1

    for i in range(n):
        if(n%s == 0):
            tot += 1
            s += 1
        if(n%s != 0):
            s += 1
    if(tot == 2):
        return True
    if(tot > 2):
        return False


n = int(input("Input number: "))
print(isPrime(n))