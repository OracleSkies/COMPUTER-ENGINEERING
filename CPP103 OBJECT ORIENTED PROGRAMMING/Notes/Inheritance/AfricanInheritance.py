class Person:
    name = ""
    ethnicity = ""
    religion = ""
    age = ""
    weight = ""

    def walk(self):
        print("I am walking")
    
    def display(self):
        print("My name is", self.name)
        print("My age is",self.age)
        print("My ethnicity is", self.ethnicity)
        print("My religion is", self.religion)

class African(Person):
    
    def walk(self):
        print("I am walking with head up")
    

class Asian(Person):

    def display(self):
        super().display()
        print("I am from Southeast Asia")

    def walk(self):
        print("I am walking with hands up")


tuason = African()
tuason.name = "Laurence Tuason"
tuason.age = 20
tuason.ethnicity = "African"
tuason.religion = "Catholic"

tuason.display()
tuason.walk()

print()

gabuyo = Asian()
gabuyo.name = "Christian Gabuyo"
gabuyo.age = 25
gabuyo.ethnicity = "Asian"
gabuyo.religion = "Christian"

gabuyo.display()
gabuyo.walk()
print()