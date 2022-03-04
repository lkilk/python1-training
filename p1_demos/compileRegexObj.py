import re

pattern = '^([0-9]{3,5}) *[0-9]{3} *[0-9]{3}$'

#  Regular expression object returned by compile method
#  provides all functions that re module provides
#  Potentially more efficient if using pattern more than once.

phoneNumberRegex = re.compile(pattern) #Returns compiled regex object

phoneNumber = input("\nEnter the phone number: ") 

mo = phoneNumberRegex.search( phoneNumber ) # Returns matched object.

#Regex pattern is stored in the regex object so pattern not required 
#as an argument to object phoneNumberRegex

if mo:
   print (f"\nNumber { mo.group()} matches regex pattern" )
else:
   print(f"\nNumber {phoneNumber}  doesn't match regex pattern" )
