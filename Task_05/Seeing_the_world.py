# The program shows how to sorted() reverse() 
# and sort() elements of a list

nice_locations = ['Kalam','Shangla top', 'Yakhtange','Kumrat']
print('The orignal list:')
print(nice_locations)

print('sorted list:')
print(sorted(nice_locations))
print("orignal list:")
print(nice_locations)

print("list in reverse order using sorted():")
print(sorted(nice_locations, reverse = True))
print("orignal list:")
print(nice_locations)

print('The order of list is reversed:')
nice_locations.reverse()
print(nice_locations)

nice_locations.reverse()
print('The order of a list is changed back to its orignal order:')
print(nice_locations)

nice_locations.sort()
print("The order of a list is changed to alphabetical order:")
print(nice_locations)

nice_locations.sort(reverse = True)
print("The order of a list is changed:")
print(nice_locations)