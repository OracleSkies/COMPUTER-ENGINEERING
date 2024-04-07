import math
class Activity: 
    def circumference(self):
        userInput = float(input("Please input the radius: "))
        circumference = 2 * math.pi * userInput
        print(f"The circumference is {circumference:.2f}\n")
run1 = Activity()
run1.circumference()
run2 = Activity()
run2.circumference()