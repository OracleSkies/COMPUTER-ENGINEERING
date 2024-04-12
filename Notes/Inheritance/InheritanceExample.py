class Animal:
    name = ""

    def eat(self):
        print("I can eat")

class Dog(Animal):
    def displayName(self):
        print("My name is ", self.name)

labrador = Dog()
labrador.name = "Chowchow"
labrador.displayName()