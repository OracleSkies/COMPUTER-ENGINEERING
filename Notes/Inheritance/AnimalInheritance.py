class Animal:
    name = ""

    def eat(self):
        print("I can eat")
    
    def jump(self):
        print("I am jumping")

class Dog(Animal):
    def displayName(self):
        print("My name is ", self.name)

    def eat(self): #overrides eat() of Animal()
        print("I love eating bones")
        super().eat() 

class Cat(Animal):
    def displayName(self):
        print("My name is ", self.name, " I am a cat")
    
    def eat(self): #overrides eat() of Animal()
        print("I love eating cat food")

labrador = Dog()
labrador.name = "Chowchow"
labrador.displayName()
labrador.eat()
labrador.jump()

persian = Cat()

persian.name = "Meowmeow"
persian.displayName()
persian.eat()
persian.jump()
