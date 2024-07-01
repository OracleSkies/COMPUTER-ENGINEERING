class Activity: 
    def feetToInch(self):
        print("You selected Feet to Inch Conversion \n")
        userInput = float(input("Please input a measurement in ft: "))
        conversion = userInput * 12
        print(f"{userInput}ft is equivalent to {conversion} \n")
run1 = Activity()
run1.feetToInch()
run2 = Activity()
run2.feetToInch()