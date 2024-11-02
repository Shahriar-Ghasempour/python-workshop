number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0

if operator == '-':
    result = number_1 - number_2
elif operator == '+':
    result = number_1 + number_2
elif operator == '*':
    result = number_1 * number_2
else:
    result = number_1 / number_2
    
print(f"{number_1} {operator} {number_2} = {result}")
