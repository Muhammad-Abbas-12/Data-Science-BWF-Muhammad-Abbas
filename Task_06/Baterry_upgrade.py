# the program show how thr cars range is increased
# when battery size is upgraded


#  class Electric_car()

class Electric_car():
    def __init__(self, make, model, year):

        self.battery_size = 70
        self.battery = Battery()

# Battery size class

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has '+ str(self.battery_size) +'-KWh battery.')

    def get_range(self):

        if self.battery_size <= 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270

        message = 'This car can go approximatly '+ str(self.range)
        message += ' miles on a full charge'
        print(message)
    def upgrade_battery(self):
        
        if (self.battery_size < 85):
            self.battery_size += 5 
            return self.battery_size


# instance
electric_car = Electric_car('tesla','s','2018')
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.upgrade_battery()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()