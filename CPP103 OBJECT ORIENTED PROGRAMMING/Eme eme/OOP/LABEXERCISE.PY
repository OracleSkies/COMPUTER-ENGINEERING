import random
import string

def hello_world():
    print ("Hello World")

def arithmetic():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    
    #addition
    sum = (num1 + num2)
    print (f"The sum of {num1} and {num2} is {sum}")
    
    #Subtraction
    difference = (num1 - num2)
    print (f"The difference of {num1} and {num2} is {difference}")
    
    #Multiplication
    product = (num1 * num2)
    print (f"The product of {num1} and {num2} is {product}")
    
    #Division
    quotient = (num1 / num2)
    print (f"The quotient of {num1} and {num2} is {quotient}")

def integers():
    user = int(input("Please enter positive or negative number: "))
    if(user>0):
        print("That's a positive number")
    else:
        print("That's a negative number")

def feet_to_inch():
    user = int(input("Please enter any number (feet): "))
    inches = (user*12)
    print(f"{inches} inches")

def circumference():
    pi = 3.1416
    
    user = int(input("Please enter the radius: "))
    circumference = (2 * pi * user)
    print (f"The circumference of the circle is {circumference}")

def fibonacci():
    user = int(input("Please enter the number of terms: "))
    num1 = 0
    num2 =1

    print(num1,num2, end=" ")

    for i in range(2, user):
        num3 = num1 + num2
        print(num3, end=" ")
        num1=num2
        num2=num3

def password():
    length = int(input("Enter length: "))
    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation

    password = ''.join([random.choice(chars) for i in range (length)])

    print("Your password is: ", password)

def reverse():
    user = input("Please enter a word: ")
    string = user[::-1]
    
    print(string)

def calculator():
    user_1 = int(input("Please enter first number: "))
    user_2 =int(input("Please enter second number: "))
    operation = (input("Please enter operation sign: "))

    if (operation == '+'):
        sum = (user_1 + user_2)
        print (sum)
    elif (operation == '-'):
        diff = user_1 - user_2
        print (diff)
    elif (operation == '*'):
        prod = user_1 * user_2
        print (prod)
    elif (operation == '/'):
        quot = user_1 / user_2
        print (quot)
    else:
        print ("Error!")

def userselection():
    print ("LABORATORY EXERCISE\n") 

    user = int(input("Please choose a number 1 to 9: "))

    if user ==1:
        hello_world()
    elif user ==2:
        arithmetic()
    elif user ==3:
        integers()
    elif user==4:
        feet_to_inch()
    elif user ==5:
        circumference()
    elif user ==6:
        fibonacci()
    elif user ==7:
        password()
    elif user ==8:
        reverse()
    elif user==9:
        calculator()
    else:
        print ("Error")

userselection()





