import re

n = int(input())

for i in range(n):
    number = input()
    if(len(number) == 10):
        x = re.findall("^[7-9]\d{9}$",number)
        if(x):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
