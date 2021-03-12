f = open("text.txt", "r")
string = ""

for i in f:
    string += i

print(string)