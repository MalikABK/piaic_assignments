from making_function import add_num, sub_num, multiply_num, divide_num


first: float= float(input("Please enter first value\n"))
second: float= float(input("Please enter second value\n"))

operations: str = input("Enter the operation (+,-,*,/)")


match operations: 
    case "+":
        result:float = add_num(first, second)
        print(result)
    case "-":
        result:float =  sub_num(first, second)
        print(result)
    case "*":
        result:float = multiply_num(first, second)
        print(result)
    case "/":
        result:float = divide_num(first, second)
        print(result)