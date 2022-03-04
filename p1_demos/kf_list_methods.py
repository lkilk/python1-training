cars = []

# Adding an element to a list
cars.append('Toyota') # allows you to a single element to the end of a list
# cars.append(['Mazda','Seat'])
cars.extend(['Mazda','Seat','Ford']) # this method allows you to add/append multiple elements
cars.insert(2,'Dacia') # Add an element at a particular index
print(cars)

# Remove elements
cars.remove('Seat')
first_element = cars.pop(1)
del cars[-1]

print('first_element:' , first_element)

print(cars)