USERNAME = "admin"
PASSWORD = "admin!@#"


username = input("username: ")
password = input("password: ")

# if username == USERNAME:
#     if password == PASSWORD:
#         print("login successful")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")
    
    
# if username == USERNAME and password == PASSWORD:
#     print("login successful")
# else:
#     print("invalid username or password")

if username == "":
    print("username cannot be empty")
elif password == "":
    print("password cannot be empty")
elif username == USERNAME and password == PASSWORD:
    print("login successful")
else:
    print("invalid username or password")