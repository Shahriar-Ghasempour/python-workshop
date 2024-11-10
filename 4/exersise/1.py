# phone book

phoneBook = []

while True:
    name = input("name (or '-1' to stop): ")
    if name == '-1':
        print("=================================================================")
        break

    phoneNumber = input("phone number: ")
    phoneBook.append([name.lower(), phoneNumber])
    print("=================================================================")


while True:
    registerName = input("Search for name (or '-1' to stop): ")

    if registerName == '-1':
        break

    found = False
    for entry in phoneBook:
        if registerName.lower() == entry[0]:
            print(f"Phone number: {entry[1]}")
            found = True
            print("=================================================================")
            break

    if not found:
        print("Name not found in phone book.")
