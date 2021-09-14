class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def getInfo(self):
        print(f"vehicle name: {self.name} Speed: {self.max_speed} mileage: {self.mileage}")

a=Vehicle("Valvo",100,15)
a.getInfo()