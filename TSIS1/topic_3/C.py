import math

a = int(input())
b = int(input())


for a in range(a,b+1):
    if(math.sqrt(a) % 2 == 0 or math.sqrt(a) % 3 == 0 or math.sqrt(a) % 5 == 0):
        print(a,end=" ")
