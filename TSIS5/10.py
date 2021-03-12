f = open("text.txt", "r")

words = f.read().split()

freq = { }

for i in words:
    freq[i] = 0

for x,y in freq.items():
    for i in words:
        if(x == i):
            y += 1
            freq.update({x : y})

print(freq)