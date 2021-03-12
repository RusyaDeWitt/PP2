file = open("text.txt", "r")
lines = file.readlines()
last_lines = lines[-1:]
print(last_lines)