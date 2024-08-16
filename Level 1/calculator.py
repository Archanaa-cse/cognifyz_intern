
def calculator():
    num1 = int(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %): ")
    num2 = int(input("Enter the second number: "))

    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else 'Error: Division by zero',
        '%': num1 % num2
    }

    result = operations.get(operator, "Invalid operator")
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
