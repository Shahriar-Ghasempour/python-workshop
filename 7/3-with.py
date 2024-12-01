with open("user.txt", "r") as file:
    for line in file.readlines():
        print(line.strip())
        