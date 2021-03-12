f = open("text.txt", "r")

words = f.read().split()

max = 0

for i in words:
    str = ""
    if(len(i) > max):
        max = len(i)
        str += i
print(str)