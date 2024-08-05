# Showing inheritance

# Restauramt class

class Restaurant():
    # defining initail method which is must
    def __init__(self, restaurant_name, cuisine_type):
        # initializing varables
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # class method
    def describe_resturant(self):
        print("Restaurant name: " + self.restaurant_name.title() + ", cuisine_type: ",self.cuisine_type.title())

    # class method
    def open_restaurant(self):
        print("The Restaurant is open.")


class Icecreame_stand(Restaurant):
    
    def __init__(self):
        
        self.flavours = ["Apple",'Mango','Stabbery','Banana']
        
    def describe_flavours(self):
        for item in range(len(self.flavours)):
            print(self.flavours[item])

# class instance 

icecreame = Icecreame_stand()
icecreame.describe_flavours()