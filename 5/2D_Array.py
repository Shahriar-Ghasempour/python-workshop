users = [["shahriar", "1234"], ['ali', '3333'], ["test", "test"]]

for user in users:
    print(f"username = {user[0]}, password = {user[1]},")

for user in users:
    for i in users:
        print(i)
