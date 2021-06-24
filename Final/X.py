a = int(input())
d = { }

all_score = 0

for i in range(a):
    s = input().split()
    name = s[0]
    score = int(s[1])
    d[name] = score
    all_score += score

for x, y in d.items():
    one = 100 // all_score
    percent = one * y
    print(x, str(percent)+"%")