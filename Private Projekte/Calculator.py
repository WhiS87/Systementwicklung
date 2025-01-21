print("Welcome\n"
      "This is a Calculator.\n"
      "Insert your first nummer, the Operator and then your second nummer.\n"
      "Numbers can also be written like this: 123.00\n"
      "Valid Operators: +, -, *, /.\n")

while True:
    user_input_a = int(input("Enter the first Number: "))
    operator = input("Enter a Operator: ")
    user_input_b = int(input("Enter the second Number: "))

    if operator == "+":
        print(user_input_a + user_input_b)
        break
    elif operator == "-":
        print(user_input_a - user_input_b)
        break
    elif operator == "*":
        print(user_input_a * user_input_b)
        break
    elif operator == "/":
        print(user_input_a / user_input_b)
        break
    else:
        print("Invalid Operator")
        print("Valid Operator are  +, -, *, /")