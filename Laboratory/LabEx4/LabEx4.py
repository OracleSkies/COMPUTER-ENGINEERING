import time
from icecream import ic
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
        self.signalRhtStatus = False
        self.signalLftStatus = False
        self.hazardLightStatus = False
        

    #toggle engine method here
    def engine(self):
        if (self.engineStatus == False):
            self.engineStatus = True
            print("Engine is powered ON!")
        else:
            if (self.currentSpeed > 0):
                print("\nIt is dangerous to turn of the engine while moving")
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

    def directionConversion(self, _degrees):
        if (_degrees >= 360 or _degrees <= -360):
            self.currentDirectionDegrees = 0

        if (_degrees == -90 or _degrees == 270):
            self.currentDirection = "East"
        elif(_degrees == -180 or _degrees == 180):
            self.currentDirection = "South"
        elif(_degrees == -270 or _degrees == 90):
            self.currentDirection = "West"
        else:
            self.currentDirection = "North"
        return self.currentDirection

    def steerLeft(self):
        if (self.currentSpeed <= 0):
            print("The car is stationary")
            print("You steered the car but it did not change its direction")
        else:
            self.currentDirectionDegrees += 90
            print("\nThe car turned left")
            print("You are now heading ", self.directionConversion(self.currentDirectionDegrees))
            #may onting deceleration dapat
        ic(self.currentDirection)
        ic(self.currentDirectionDegrees)

    def steerRight(self):
        if (self.currentSpeed <= 0):
            print("The car is stationary")
            print("You steered the car but it did not change its direction")
        else:
            self.currentDirectionDegrees -= 90
            print("\nThe car turned right")
            print("You are now heading", self.directionConversion(self.currentDirectionDegrees))
            #may onting deceleration dapat
        ic(self.currentDirection)
        ic(self.currentDirectionDegrees)
    
    def signalRight(self):
        if(self.signalRhtStatus == False):
            self.signalRhtStatus = True
            print("Right turn signal ACTIVE")
        else:
            self.signalRhtStatus = False
            print("Right turn signal INACTIVE")

    def signalLeft(self):
        if(self.signalLftStatus == False):
            self.signalLftStatus = True
            print("Left turn signal Active")
        else:
            self.signalLftStatus = False
            print("Left turn signal INACTIVE")
    
    def hazardLight(self):
        return

class Assistance:
    def instructions(self):
        print("\n Here are the following commands for the car:")
        print("\neng: Toggle car ENGINE")
        print("acc: ACCELERATE")
        print("brk: BRAKE")
        print("lft: Turn LEFT")
        print("rht: Turn RIGHT")
        print("slr: Toggle RIGHT TURN SIGNAL")
        print("sll: Toggle LEFT TURN SIGNAL")
        print("wip: Toggle WIPERS")
        print("hdl: Toggle HEADLIGTS")
        print("hzl: Toggle HAZARD LIGHTS")
        print("quit: QUIT the simulation")
        print("\nOther commands:")
        print("help: show all commands")
        print("status: show all current information about your car")
    def carStatus(self):
        return

#class externalconditions
# the path leads straight ahead
    

myCar = Car("Mitsubishi", "Mirage G4", "Titanium Gray", 100, 15) 
print("CAR DETAILS: ")
print("Car Make: " , myCar.make)
print("Car Model: " , myCar.model)
print("Color: " , myCar.color)
print("Top Speed: " , myCar.topSpeed , " km/h")
print("Acceleration: " , myCar.acceleration , "kph/s")


#welcome to car driving simulation echu chu
#instructions: eng, acc, brk, lft, rht, wip, hdl, slr, sll , hzl
#for instruction: help
#for car status: status
assist = Assistance()
assist.instructions()
while True:
    userInput = input("Please select an action: ")
    if(userInput == "eng"):
        myCar.engine()
    elif(userInput == "acc"):
        myCar.accelerate()
    elif(userInput == "brk"):
        myCar.brake()
    elif(userInput == "lft"):
        myCar.steerLeft()
    elif(userInput == "rht"):
        myCar.steerRight()
    elif(userInput == "sll"):
        myCar.signalLftStatus()
    elif(userInput == "slr"):
        myCar.signalRhtStatus()
    elif(userInput == "wip"):
        myCar.wiper()
    elif(userInput == "hdl"):
        myCar.headlight()
    elif(userInput == "hzl"):
        myCar.hazardLight()
    elif(userInput == "quit"):
        return
    elif(userInput == "help"):
        assist.instructions()
    elif(userInput == "status"):
        assist.carStatus()
    else:
        break


"""
while True:
    print("\n Operation Options: ")
    print("1. Toggle Engine")
    print("2. Accelerate")
    print("3. Brake")
    print("4. Left Steer")
    print("5. Right Steer")
    print("6. Toggle Headlights")
    print("7. Toggle Wipers")

    userInput = int(input("Please select an operation number: "))
    if (userInput == 1):
        myCar.engine()
    elif(userInput == 2):
        myCar.accelerate()
    elif(userInput == 3):
        myCar.brake()
    elif(userInput == 4):
        myCar.steerLeft()
    elif(userInput == 5):
        myCar.steerRight()
    elif(userInput == 6):
        myCar.headlight()
    elif(userInput == 7):
        myCar.wiper()
    else:
        break
"""


