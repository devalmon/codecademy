class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def drive_car(self):
        self.condition = "used"
    
    def display_car(self):
        result = "This is a {} {} with {} MPG.".format( self.color, self.model, str(self.mpg))
        print result

my_car = Car("DeLorean", "silver", 88)

print my_car.condition
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.battery_type = battery_type
        return super(ElectricCar, self).__init__(model, color, mpg)
    
    def drive_car(self):
        self.condition = "like new"
        
my_car = ElectricCar("Tesla", "black", 120,"molten salt")

my_car.drive_car()
print my_car.condition
