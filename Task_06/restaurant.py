# restaurant class in module restaurant

# class restauant

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
