# A set is an unordered collections of items. Each element in a set
# is unique and cannot be changed. The set itself is mutable i.e.
# elements can be added or removed.

# Defined using {} ( since 2.6 ) or the set function

set1 = { 'a','b','c' }

print( '\nset1: ' , set1 ) 

# The elements can be of different datatypes 
set2 = { 'a', 10, 3.14, ('joe','Jane') }

print( '\nset2: ' , set2 )

# Cannot include a mutable item
# Gives an error
# TypeError: unhashable type: 'list'
# set3 = { 'a', 10, 3.14, ['Joe','Jane'], ('car','shed')  }

# Can create a set from a list as follows:

set3 = set(['John','Jill', 'Jane', 'Sidney', 'Jill' ] )
print( '\nset3: ' , set3 )

# Creating an empty is as follows:

set4 = set() 

# set4 = {} will create an empty dictionary

# Sets do not support slicing or indexing
# Can use add methods to add a single (immutable) element

print ( '\nUsing add method on set3' )

set3.add( 'Ciara' )
print('Set3: ' , set3 )

# Can use update method to add many items
# Update accepts strings,tuples,lists and sets
print ( '\nUsing update method on set3' )

set3.update( ['dog', 'cat'],('eagle','budgie')) 
print('Set3: ' , set3 )

# Use the discard or remove method to remove a element
# remove raises error if element does  not exist

print ( '\nRemoving dog from set3' )

set3.remove( 'dog' )
print('Set3: ' , set3 )

#A frozen set is immutable
fset = frozenset(['a','b','c','d'])