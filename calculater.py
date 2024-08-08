first_value: float = float(input("Please enter first value\n"))

second_value: float = float(input("Please enter second value\n"))

operations: str = input("Enter the operation (+, -, *, /): ")

print(type(first_value))

match operations: 
    case "+":
        print(f"the sum of {first_value} and {second_value} is {first_value + second_value}")
    case "-":
        print(f"the difference of {first_value} and {second_value} is {first_value - second_value}")
    case "*":
        print(f"the product of {first_value} and {second_value} is {first_value * second_value}")
    case "/":
        if second_value == 0:
            print("Error: Division by zero")
        else:
            print(f"the quotient of {first_value} and {second_value} is {first_value / second_value}")