#  Making a simple class of two variables and one method

from restaurant import Restaurant

# instance
my_restaurant = Restaurant("Darbar Hotel",'better')

# printint class attribute
print(my_restaurant.restaurant_name)
# printing class attribute
print(my_restaurant.cuisine_type)

# calling method
my_restaurant.describe_resturant()
# calling method
my_restaurant.open_restaurant()       