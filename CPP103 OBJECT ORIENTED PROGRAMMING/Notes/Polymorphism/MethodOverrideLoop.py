class Car:
    def move(self):
        print("Drive")


class Boat:
    def move(self):
        print("Sail")

class Plane:
    def move(self):
        print("Fly")


kotse = Car()
banka = Boat()
eroplano = Plane()

for vehicle in (kotse, banka, eroplano):
    vehicle.move()