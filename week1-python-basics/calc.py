import sys

# Check we have exactly 4 arguments: script name + 3 inputs
if len(sys.argv) != 4:
    print("Usage: <num1> <num2> <operation>")
    print("Operations: add, subtract, multiply, divide")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3].lower()
8 
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        sys.exit(1)
    result = num1 / num2
else:
    print(f"Unknown operation: {operation}")
    sys.exit(1)

print(f"{num1} {operation} {num2} = {result}")