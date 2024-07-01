class Vehicle:
    def move(self, name = None):
        self.name = name

        if self.name == None:
            print("Drive")
        else:
            print(f"{self.name} is now moving")

kotse = Vehicle()
kotse.move() #poly can accept null values and can still run
kotse.move("Toyota") #This is the "new form" of Vehicle

user = input()
kotse.move(user) #accepts user input