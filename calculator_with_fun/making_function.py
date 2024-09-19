def add_num(first_value,second_value)  ->float:
    print(f"the sum of {first_value} and {second_value} is: ")
    return  first_value + second_value

def sub_num(first_value,second_value)->float:
    print(f"the difference of {first_value} and {second_value} is: ")
    return  first_value-second_value

def multiply_num(first_value,second_value) -> float:
    print(f"the product of {first_value} and {second_value} is:")
    return first_value * second_value

def divide_num(first_value, second_value) -> float:
    if second_value == 0:
        print("Error: Division by zero")
    print(f"the division of {first_value} and {second_value} is:")
    return  first_value / second_value
    