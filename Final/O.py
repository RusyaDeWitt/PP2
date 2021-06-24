s = input().split()
max = 0
word = ""

for i in s:
    tmp = 0
    for j in s:
        if(i.upper() == j.upper()):
            tmp += 1
    if(tmp > max):
        max = tmp
        word = ""
        word += i.upper()

print(word)