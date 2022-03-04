set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7 }

print("\nset_a:" , set_a )
print("set_b:" , set_b )

# Use the intersection_update method to remove members from set_a not in set_b
set_a.intersection_update(set_b)  # Does not return anything, changes set_a

print('\nIntersection_update: ' , set_a )

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7 }

# Use the difference_update method to remove members from set_a that are also in set_b
set_a.difference_update(set_b) 

print('\ndifference_update: ' , set_a )

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7 }

# Use the symmetric_difference_update method to remove members from set_a that exist in 
# both set_a and set_b 

set_a.symmetric_difference_update(set_b) 
print('\nsymmetric_difference_update: ' , set_a  )

set_a = {1, 2}
set_b = {1,2, 7, 8,9 , 10 }
set_c = {4,5,6}

# isdisjoint returns True if intersection of 2 sets returns an empty set 
print( f'\n{set_a} is disjoint of {set_b} - {set_a.isdisjoint(set_b)}')

print( f'\n{set_a} is disjoint of {set_c} - {set_a.isdisjoint(set_c)}')

print( f'\n{set_a} is subset of {set_b} - {set_a.issubset(set_b)}')

print( f'\n{set_b} is superset of {set_a} - {set_b.issuperset(set_a)}')



