import time
class Car:

    #constructor
    def __init__(self, make = "", model = "", color = "", topSpeed = 0, acceleration = 0):
        self.make = make
        self.model = model
        self.color = color
        self.topSpeed = topSpeed
        self.acceleration = acceleration
        self.engineStatus = False
        self.currentSpeed = 0
        self.headlightStatus = False
    
    def startEngine(self):
        if(self.engineStatus == False):
            self.engineStatus = True
            print("Engine is powered ON!")
        else:
            print("Engine is already ON!")

    def stopEngine(self):
        if(self.engineStatus == True):
            self.engineStatus = False
            print("Engine is powered OFF!")
        else:
            print("Engine is already OFF!")
    
    def accelerate(self):
        if (self.engineStatus == True):
            while(self.currentSpeed < self.topSpeed):
                time.sleep(0.1)    
                self.currentSpeed += self.acceleration
                print("Current Speed: ", self.currentSpeed)
                if(self.currentSpeed == self.topSpeed):
                    print("Top speed reached!")
        else:
            print("Car cannot accelerate! Your car is OFF!")

    def brake(self):
        if(self.currentSpeed <= 0):
            print("Car already stopped")
        else:
            while(self.currentSpeed > 0):
                time.sleep(0.1)
                self.currentSpeed -= 10
                print("Current Speed: ", self.currentSpeed)
                if(self.currentSpeed == 0):
                    print("Car now stopped")
    def headlight(self):
        return


myCar = Car("Mitsubishi", "Mirage G4", "Titanium Gray", 100, 5) 
print("CAR DETAILS: ")
print("Car Make: " , myCar.make)
print("Car Model: " , myCar.model)
print("Color: " , myCar.color)
print("Top Speed: " , myCar.topSpeed , " km/h")
print("Acceleration: " , myCar.acceleration , "kph/s")

while True:
    print("\n Operation Options: ")
    print("1. Start Engine")
    print("2. Stop Engine")
    print("3. Accelerate")
    print("4. Brake")

    userInput = int(input("Please select an operation number: "))
    if (userInput == 1):
        myCar.startEngine()
    elif(userInput == 2):
        myCar.stopEngine()
    elif(userInput == 3):
        myCar.accelerate()
    elif(userInput == 4):
        myCar.brake()
    else:
        break


