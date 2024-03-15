class Activity: 
    def positiveCheck(self):
        print("You selected Positive or Negative Program \n")
        userInput = float(input("Please input a number: "))
        if userInput >= 0:
            print(f"{userInput} is a positive number")
        elif userInput < 0:
            print(f"{userInput} is a negative number")
        else:
            print("error")
        print("")
run1 = Activity()
run1.positiveCheck()
run2 = Activity()
run2.positiveCheck()