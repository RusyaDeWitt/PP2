f = open("text.txt", "a")

f.write("Hello there")
f.close()

f = open("text.txt")
print(f.read())