# making a function w all operators 
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Error! Division by zero."
    else:
        return "Invalid operation"

#input
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Displae result
result = calculate(num1, num2, operation)
print(f"Result: {result}")