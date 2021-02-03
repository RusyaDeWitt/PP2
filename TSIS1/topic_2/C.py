n = input()
ans = int(input())

if(len(n) == 4):
    if(n == reversed(n)):
        if(ans == 1):
            print("YES")
        else:
            print("NO")
else:
    print("NO")
