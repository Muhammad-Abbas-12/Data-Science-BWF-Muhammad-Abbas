# The show all the functions in chapter 03 applied to a list

cities = ['Islamabad','Peshawar','Faisalabad','Karachi','Lahore','Jhang']
print('The orignal list:')
print(cities)
print(f'Lenth of orignal list \n{len(cities)}')   # printing lenth of a list items

print('Printing list items one by one:')      # printing list items one by one
for items in range(len(cities)):
    print(f"{cities[items]}\n")

cities = sorted(cities)   # sorting list using sorted() in alphbetical order
print('Sorting list item using sorted() in alphbetical order:')
print(cities)

cities = sorted(cities, reverse = True)   # sorting list using sorted() in reverse order using reverse as augument
print('Sorting list item using sorted() in resverse order:')
print(cities)

cities.sort()    # sorting list using sort() in alphabetical order
print("sorting list items using sort() in alphabetical order:")
print(cities)

cities.sort(reverse = True)   # sorting list items using sort() in reverse order
print('Sorting list item using sort() in reverse order')
print(cities) 

cities.reverse()   # reversing list items
print('Reversing list items:')
print(cities)

print('Inserting an item in list at specific position:')
cities.insert(1, "Malakand")     # Inserting item in list at specific position
print(cities)
print('Inserting an item at the end of a list:')
cities.append("Maingora")        # Inserting item in list at the end of the list 
print(cities)
print('Deleting an item at the end of a list:')
cities.pop()                     # Deleting an item at the end of a list
print(cities)
print("Deleting an item at specific position:")
del cities[0]                    # Deleting an item at specific position
print(cities)
