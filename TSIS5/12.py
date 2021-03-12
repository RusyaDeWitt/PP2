f = open("text2.txt", "w")

list = ["hello" , "world"]

for i in list:
    f.write(i)
f.close()

f = open("text2.txt","r")

print(f.read())