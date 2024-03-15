class Activity: 
    def calculator(self):
        print("You selected Calculator Program \n")
        intInput1 = float(input("Please enter first number: "))
        intInput2 = float(input("Please enter second number: "))
        operator = input("Select an operator (+, -, *, /): ")

        if operator == "+":
            sumInt = intInput1 + intInput2
            print(sumInt)
        elif operator == "-":
            diff = intInput1 - intInput2
            print(diff)
        elif operator == "*":
            prod = intInput1 * intInput2
            print(prod)
        elif operator == "/":
            quo = intInput1 / intInput2
            print(quo)
        else:
            print("error")
        print("")
run1 = Activity()
run1.calculator()
run2 = Activity()
run2.calculator()