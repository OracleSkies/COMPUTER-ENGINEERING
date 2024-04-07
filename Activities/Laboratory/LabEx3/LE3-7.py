import string
import random
class Activity: 
    def passwGen(self):
        print("You selected Password Generation Program \n")
        passLenInput = int(input("Please input the length of your password: "))

        char = string.ascii_letters + string.digits + string.punctuation
        randString = ''.join(random.choices(char, k=passLenInput))
        print(randString)
        print("")
run1 = Activity()
run1.passwGen()
run2 = Activity()
run2.passwGen()