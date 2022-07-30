print("Simple Calculator")
first_digit = input("input first operand!\n")
first_digit_int = float(first_digit)
operation = input("what operator will you like to use +, -, * or / ?\n")
second_digit = input("input second operand!\n")
second_digit_int = float(second_digit)
if operation == "+":
    print("Your answer is: ""{:.2f}".format(first_digit_int + second_digit_int))
elif operation == "-":
    print("Your answer is: ""{:.2f}".format(first_digit_int - second_digit_int))
elif operation == "*":
    print("Your answer is: ""{:.2f}".format(first_digit_int * second_digit_int))
elif operation == "/":
    print("Your answer is: ""{:.2f}".format(first_digit_int / second_digit_int))
else:
    print("Error!")
