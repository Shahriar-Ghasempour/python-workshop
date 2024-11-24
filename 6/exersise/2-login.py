userDB = []

def Auth():
    action = input("login or signup: ").lower().strip()
    
    if action == "signup":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        for user in userDB:
            if user['username'] == username:
                print("Username already exists. Please try a different one.")
                return
        
        userDB.append({"username": username, "password": password})
        print("Signup successful! You can now login.")
    
    elif action == "login":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        for user in userDB:
            if user['username'] == username and user['password'] == password:
                print("Login successful! Welcome back.")
                return
        print("Invalid username or password.")
    
    else:
        print("Invalid action. Please choose 'login' or 'signup'.")

while True:
    Auth()
    answer = input("Do you want to continue? (yes/no): ").lower().strip()
    if answer == "yes":
        continue

    elif answer == "no":
        print("Goodbye!")
        break

    else:
        print("Invalid answer. Please choose 'yes' or 'no'.")
        continue
