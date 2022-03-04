deep_purple = { 'Gillan', 'Blackmore',
                'Paice','Glover','Lord'
              }

rainbow = { 'Dio','Driscoll' , 
            'Glover', 'Soule',
            'Blackmore'
          }

print('Deep Purple Members: ' , deep_purple )

print ('\nRainbow Members: ' , rainbow )

# Use the union method to get a distinct union
print('\nAll Members of both bands: ' , deep_purple.union(rainbow) )

# Use the intersection method to get an intersection
print('\nShared Members: ' , deep_purple.intersection(rainbow) )

# Use the difference method to get members in one set only
print('\nPurple Only: ' , deep_purple.difference(rainbow) )

# Use the symmetric_difference method to get non-shared members in both sets
print('\nNon Shared Members: ' , deep_purple.symmetric_difference(rainbow) )

# Use the clear method to empty a set
deep_purple.clear()
print('\nPurple after clear: ' , deep_purple )

# Use the pop method to randomly remove an element from a set
one_less = rainbow.pop()
print('\nRainbow lose a random member: ' , rainbow )
