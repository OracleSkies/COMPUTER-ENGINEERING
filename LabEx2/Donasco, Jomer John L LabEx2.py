import math
import random
import string

def helloWorld():
    print("You selected Hello World Program \n")
    message = "Hello World"
    print(message)

def arithmetic():
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

def positiveCheck():
    print("You selected Positive or Negative Program \n")
    userInput = float(input("Please input a number: "))
    if userInput >= 0:
        print(f"{userInput} is a positive number")
    elif userInput < 0:
        print(f"{userInput} is a negative number")
    else:
        print("error")

def feetToInch():
    print("You selected Feet to Inch Conversion \n")
    userInput = float(input("Please input a measurement in ft: "))
    conversion = userInput * 12
    print(f"{userInput}ft is equivalent to {conversion}")

def circumference():
    userInput = float(input("Please input the radius: "))
    circumference = 2 * math.pi * userInput
    print(f"The circumference is {circumference:.2f}")

def fibonnacci():
    print("You selected Fibonacci Sequence Program \n")
    terms = int(input("Please input the number of terms: "))
    first = 0
    second = 1
    print(first, second, end=" ")
    for count in range(2, terms):
        c = first + second
        print(c, end=" ")
        first = second
        second = c

def passwGen():
    print("You selected Password Generation Program \n")
    passLenInput = int(input("Please input the length of your password: "))

    char = string.ascii_letters + string.digits + string.punctuation
    randString = ''.join(random.choices(char, k=passLenInput))
    print(randString)

def reverse():
    print("You selected Reverse String Program \n")
    string = input("Please input anything: ")
    print(string[::-1])

def calculator():
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
    

def userSelectFuntion(): #pipili si user ng function na irurun
    print("LABORATORY EXERCISE\n")
    print("Available Programs: \
        \n1. Hello World \
        \n2. Arithmetic\
        \n3. Positive or Negative Integer \
        \n4. Feet to Inch Conversion\
        \n5. Circumference\
        \n6. Fibonacci Sequence\
        \n7. Random Password Generator\
        \n8. String Reverse\
        \n9. Calculator \n")
    userSelect = int(input("Please select a number corresponding to the program you want to run: "))
    if userSelect == 1:
        helloWorld()
    elif userSelect == 2:
        arithmetic()
    elif userSelect == 3:
        positiveCheck()
    elif userSelect == 4:
        feetToInch()
    elif userSelect == 5:
        circumference()
    elif userSelect == 6:
        fibonnacci()
    elif userSelect == 7:
        passwGen()
    elif userSelect == 8:
        reverse()
    elif userSelect == 9:
        calculator()
    else:
        print("Error try again")

userSelectFuntion()


