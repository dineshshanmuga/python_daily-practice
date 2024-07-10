operator = input("Enter the operator (+ - * /): ")
num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1*num2
    print(round(result,3))
elif operator == "/":
    result = num1/num2
    print(round(result,3))
else:
    print(f'The given {operator} is a INVALID operator')