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
        self.wiperStatus = False
        self.currentDirection = "North"
        self.currentDirectionDegrees = 0

    #toggle engine method here
    def engine(self):
        if (self.engineStatus == False):
            self.engineStatus = True
            print("Engine is powered ON!")
        else:
            if (self.currentSpeed > 0):
                print("It is dangerous to turn of the engine while moving")
                print("Stop the car first before turing the ENGINE OFF")
            else:
                self.engineStatus = False
                print("Engine is powered OFF!")
    
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
            print("Car is stationary")
        else:
            while(self.currentSpeed > 0):
                time.sleep(0.1)
                self.currentSpeed -= 10
                print("Current Speed: ", self.currentSpeed)
                if(self.currentSpeed == 0):
                    print("Car now stopped")

    def headlight(self):
        #engine must be activated first
        if (self.engineStatus == False):
            print("\n Engine is OFF")
            print("\n Activate the ENGINE first")
            return
        else:
            if (self.headlightStatus == False):
                self.headlightStatus = True
            else:
                self.headlightStatus = False
            
            if (self.headlightStatus == True):
                print("Headligts are ON!")
            else: 
                print("Headlights are OFF!")

    def wiper(self):
        #engine must be activated first
        if (self.engineStatus == False):
            print("\n Engine is OFF")
            print("\n Activate the ENGINE first")
        else:
            if (self.wiperStatus == False):
                self.wiperStatus = True
            else:
                self.wiperStatus = False
            
            if (self.wiperStatus == True):
                print("Wipers are ACTIVE!")
            else: 
                print("Wipers are INACTIVE!")
    def steerRight(self):
        return
    def steerLeft(self):
        return
    def signalRight(self):
        return
    def signalLeft(self):
        return

#class ExternalCondition:
# the path leads straight ahead
    

myCar = Car("Mitsubishi", "Mirage G4", "Titanium Gray", 100, 5) 
print("CAR DETAILS: ")
print("Car Make: " , myCar.make)
print("Car Model: " , myCar.model)
print("Color: " , myCar.color)
print("Top Speed: " , myCar.topSpeed , " km/h")
print("Acceleration: " , myCar.acceleration , "kph/s")


#welcome to car driving simulation echu chu
#instructions: eng, acc, brk, left, right, wip, hli
#for instruction: help
#for car status: status
while True:
    print("\n Operation Options: ")
    print("1. Start Engine")
    print("2. Stop Engine")
    print("3. Accelerate")
    print("4. Brake")
    print("5. Toggle Headligts")
    print("6. Toggle Wipers")

    userInput = int(input("Please select an operation number: "))
    if (userInput == 1):
        myCar.engine()
    elif(userInput == 2):
        myCar.stopEngine()
    elif(userInput == 3):
        myCar.accelerate()
    elif(userInput == 4):
        myCar.brake()
    elif(userInput == 5):
        myCar.headlight()
    elif(userInput == 6):
        myCar.wiper()
    else:
        break


