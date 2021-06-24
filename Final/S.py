a = int(input())
s = input().split()
n = []
max = 0

for i in s:
    if(int(i) > max):
        max = int(i)

for i in s:
    if(i != str(max)):
        n.append("0")
    if(i == str(max)):
        n.append("1")

for i in n:
    print(i,end=" ")