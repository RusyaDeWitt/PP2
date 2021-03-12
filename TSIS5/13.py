f = open("text.txt", "r")
d = open("text2.txt", "w")

str = f.read()
str2 = ""
str2 += str
d.write(str2)

d.close()
d = open("text2.txt", "r")
print(d.read())
