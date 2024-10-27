while True:
    number = int(input("enter number: "))
    if number % 2 ==0:
        print(f"{number} % 2 = 0")

    elif number < 0:
        break
    
    else:
        print(f"{number} % 2 != 0")