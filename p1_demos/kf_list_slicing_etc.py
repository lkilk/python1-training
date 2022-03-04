cars = ['Toyota', 'Mazda', 'Dacia', 'Seat', 'Ford','BMW','Volvo','Vauxhall']

print('Elements:' , len(cars) )

cars[1] = 'Skoda'
print('cars:', cars )
# Slicing can be applied to any indexed collection
# it allows us to create a new collection as a subset of an existing collection
print('first 2:', cars[0:2] ) 
print('first 2:', cars[:2] ) # shorthand for the example directly above

print('From 4th element t0 7th element:', cars[4:8] ) 
print('From 4th element to the end:', cars[4:] )

print('using -ve indexes:', cars[-5:-2] )

print('Every second element:', cars[0:len(cars):2] ) 
print('Every second element (shorthand):', cars[::2] )

# Can also use slicing to remove from and update to an existing list 
# To update

cars[2:4] = ['Audi','Fiat']
print('cars after multiple update:' , cars )

# To delete
del cars[2:4]
print('cars after multiple delete:' , cars )
