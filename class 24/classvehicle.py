# class vehicle
class vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed = max_speed
        self.milage = milage
modelx = vehicle(250,20)
print("vehicle speed is",modelx.max_speed)
print("vehicle milage is",modelx.milage)