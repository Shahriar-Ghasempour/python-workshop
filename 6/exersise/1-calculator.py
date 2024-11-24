number_1 = int(input())
number_2 = int(input())
operator = input()

def calculator(numOne, numTwo, operator):
    if operator == '-':
        return numOne - numTwo
    
    elif operator == '+':
        return numOne + numTwo
    
    elif operator == '*':
        return numOne * numTwo
    
    elif operator == '/':
        return numOne / numTwo
    
    else:
        return "Invalid Operation"


print(calculator(number_1, number_2, operator))
