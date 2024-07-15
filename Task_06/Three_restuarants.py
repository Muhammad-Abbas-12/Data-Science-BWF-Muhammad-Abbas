# Making three instinces of a class Retaurant

class Restaurant():
    # difining initial method which is must
    def __init__(self, restaurant_name, cuisine_type):
        self.retaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name: '+ self.retaurant_name.title() + ', Cusine type: '+ self.cuisine_type.title())

    def open_restaurant(self):
        print('The Restaurant is open')


# class instance
restaurant_1 = Restaurant('macdonald', 'excellent')
restaurant_1.describe_restaurant()

# class instance
restaurant_2 = Restaurant('KPC','excellent')
restaurant_2.describe_restaurant()

# class instance
restaurant_3 = Restaurant('the monal islamabad','better')
restaurant_3.describe_restaurant()
        