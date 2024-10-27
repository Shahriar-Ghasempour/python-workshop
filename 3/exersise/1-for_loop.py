numberOne = int(input("number 1: "))
numberTwo = int(input("number 2: "))

if numberOne >= numberTwo:
    print("Error: num1 bigger than or Equal to num2")
else:
    for i in range(numberOne, numberTwo):
        print(i)
