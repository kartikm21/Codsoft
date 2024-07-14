def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print("Select the operation to perform\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division")

operator = int(input("Select from 1, 2, 3, 4: "))

num1 = float(input("Enter the 1st value: "))
num2 = float(input("Enter the 2nd value: "))

if operator == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif operator == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif operator == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operator == 4:
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid response")
