class Activity: 
    def arithmetic(self):
        print("You selected Arithmetic Program \n")
        intInput1 = float(input("Please input first number: "))
        intInput2 = float(input("Please input second number: "))
        sumInt = intInput1 + intInput2
        diff = intInput1 - intInput2
        prod = intInput1 * intInput2
        quo = intInput1 / intInput2

        print(f"The sum is {sumInt}")
        print(f"The difference is {diff}")
        print(f"The product is {prod}")
        print(f"The quotient is {quo}")
        print("")
run1 = Activity()
run1.arithmetic()
run2 = Activity()
run2.arithmetic()