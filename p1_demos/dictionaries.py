# Create an empty dictionary
myDictDemo = {}

# Add individual key/value pair elements
# Keys and values 

myDictDemo['one'] = "This is one"
myDictDemo[2] = "This is two"
myDictDemo['three'] = 3

print ( myDictDemo )

# Create dictionary with key/value pair elements 
myDictDemo={'name' : 'Algernon' ,'id' : 3123, 'department': 'Training'}

# Access the value using the key

print( 'Name: ' , myDictDemo['name'] )

# Dictionary 
person = {
    "name" : "James Peter",
    "age" : 21,
    "address" : { 'street': '111 Skeleton Avenue',
                  'district':'Leytonstone',
                  'town':'London'
    },
    "hobbies" : [ "reading", "walking" ]
}

# print( "\nName: %s Street: %s Hobby: %s" %( person['name'] , 
#          person['address']['street'], person['hobbies'][1]) )

print( f"\nName: {person['name']} Street: {person['address']['street']} Hobby: {person['hobbies'][1]}")
