f = open("user.txt", "r")
# content = f.readlines()
for line in f.readlines():
    print(line.strip())

f.close()