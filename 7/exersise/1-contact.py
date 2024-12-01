def load_phonebook(filename):
    phone_book = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone_number = line.strip().split(',')
                phone_book.append([name, phone_number])
    except FileNotFoundError:
        print("Phone book file not found. Starting with an empty phone book.")
    return phone_book

def save_phonebook(filename, phone_book):
    with open(filename, 'w') as file:
        for entry in phone_book:
            file.write(f"{entry[0]},{entry[1]}\n")

def write_mode(phone_book):
    while True:
        name = input("name (or '-1' to stop): ")
        if name == '-1':
            print("=================================================================")
            break
        phone_number = input("phone number: ")
        phone_book.append([name.lower(), phone_number])
        print("=================================================================")
    return phone_book

def read_mode(phone_book):
    while True:
        register_name = input("Search for name (or '-1' to stop): ")
        if register_name == '-1':
            break
        found = False
        for entry in phone_book:
            if register_name.lower() == entry[0]:
                print(f"Phone number: {entry[1]}")
                found = True
                print("=================================================================")
                break
        if not found:
            print("Name not found in phone book.")
            print("=================================================================")


filename = "phonebook.txt"
phone_book = load_phonebook(filename)
    
while True:
    mode = input("Choose mode: 'read' or 'write' (or '-1' to exit): ").strip().lower()
    if mode == '-1':
        break
    elif mode == 'write':
        phone_book = write_mode(phone_book)
        save_phonebook(filename, phone_book)
    elif mode == 'read':
        read_mode(phone_book)
    else:
        print("Invalid mode. Please enter 'read' or 'write'.")
print("=================================================================")
