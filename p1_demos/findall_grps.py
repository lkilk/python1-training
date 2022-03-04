import re

file_contents = "David Smith,500.0 Sarah Jones,-150.0 Tom Wilson,2000.0 Jane Thompson,275.0 Simon Davis,100.0"

pattern1 = "[a-z]+,\d{3,4}" # matching surname,balance as pattern within string ie Smith,500
pattern2 = "([a-z]+),(\d{3,4})" # Defining surname and balance as sub groups within pattern to match

match1 = re.findall(pattern1, file_contents, re.I)  #  Each match returned as element in a list
match2 = re.findall(pattern2, file_contents, re.I)  #  Each match returned as a 2 element tuple in a list

print( f"\nWithout grouping: {match1}" )
print( f"With grouping: {match2}\n" )

#for name,balance in match2:
#    print(f"Name: {name:9} - Balance: {balance}")