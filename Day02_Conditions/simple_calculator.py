# Take two number inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Take operator input
print("Select operation: +, -, *, /")
operator = input("Enter operator: ")

# Perform operation based on the choice
if operator == "+":
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator!")
