# Extention of Restauranat class with number served and
# set_number_served

class Restaurant():
    # defining initail method which is must
    def __init__(self, restaurant_name, cuisine_type):
        # initializing varables
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # class method
    def describe_resturant(self):
        print("Restaurant name: " + self.restaurant_name.title() + ", cuisine_type: ",self.cuisine_type.title())

    # class method
    def open_restaurant(self):
        print("The Restaurant is open.")


    # class method
    def set_number_served(self, number_of_cutomer):
        print("The number of customers "+ self.restaurant_name +" has served are: ", number_of_cutomer) 
        
    # class method\
    def increment_number_served(self,increment_customer):
        total_customer = self.number_served + increment_customer
        print("The total number of customers served in today of business are: ",total_customer)

# class instance
restaurant = Restaurant('macdonald','excellent')
restaurant.number_served
print("The number of customer the restaurant has serverd are: ",restaurant.number_served)
restaurant.number_served = 5
print("The number of customer the reataurant has served are: ",restaurant.number_served)
restaurant.set_number_served(55)
restaurant.increment_number_served(67)

