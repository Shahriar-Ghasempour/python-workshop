import json

def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)
    print("Contacts have been saved.")

def load_contacts(filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        print("File not found. No data exists.")
        return []

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact = {'name': name, 'phone': phone}
    contacts.append(contact)
    print("Contact has been added.")

def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("List of contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone']}")

contacts = load_contacts()

while True:
    print("\n1. Add a contact")
    print("2. Display contacts")
    print("3. Exit")
    choice = input("Please enter your choice: ")

    if choice == '1':
        add_contact(contacts)
        save_contacts(contacts)
    elif choice == '2':
        display_contacts(contacts)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
