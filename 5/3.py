users = []
while True:
    user = {
        "username": "",
        "password": "",
        "email": "",
        "phone": ""
    }

    for key in user:
        userInput = input(f"enter {key}: ")

        if userInput == "-1":
            print(user)
            break

    user[key] = userInput


users.append(user)
