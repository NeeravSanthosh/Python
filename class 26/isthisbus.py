class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class bus(vehicle):
    pass
bus = bus("volve",185,20)
print("vehicle name",bus.name,"speed",
bus.maxspeed,"mileage",bus.mileage)