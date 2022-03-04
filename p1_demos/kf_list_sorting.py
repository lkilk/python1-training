cars = ['Toyota', 'Mazda', 'Dacia', 'Seat', 'Ford','BMW','Volvo','Vauxhall']

print("Cars before sort:\n" , cars )

# The sort method can be used to sort a list ( in place )

cars.sort()
print("\nAfter cars.sort():\n" , cars )

cars.sort(reverse=True)
print("\nAfter cars.sort(reverse=True):\n" , cars )

cars.sort(key=len)
print("\nAfter cars.sort(key=len):\n" , cars )

cars.sort(key=len,reverse=True)
print("\nAfter cars.sort(key=len,reverse=True):\n" , cars )
