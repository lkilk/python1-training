#  Numeric datatypes
age = 31 #  Interger object references by the age variable 
age = 'Thirty One' #  Age variable now references a string object 
price = 9.99 #  Float object created
over18 = True #  Boolean object created using built in constant True (False also available)
my_complex = 2 + 3j 
my_binary = 0b1101 #  Binary object
print('my_binary:', my_binary) #  Print binary number converted to int
print('my_binary:', bin(my_binary)) #  Print binary number in binary format

#  Collections - can be indexed or non-indexed
name = 'Liam'
print('First character:' , name[0])
names_list = ['Liam','Roger','Phil','Sebastian'] #  A list is similar to an array, it can be altered
names_tuple = ('Liam','Roger','Phil','Sebastian') #  A tuple object cannot be altered 

#  Non-indexed collections 
namesSet = {'Liam','Roger','Phil','Sebastian','Liam','Liam'} #  An unordered colletion of unique values
print('Names Set', namesSet)

details_dictionary = {'id':1234 , 'first_name':'Brian', 'last_name':'Short',
            'address': {'house_number':111, 'street':'Skeleton Avenue'},
            'hobbies':['Reading','Walking','Cinema','Concerts']
            }

print(details_dictionary['id']) #   Pass in the name of key that you would like to retrieve the value of
print('House number:', details_dictionary['address']['house_number'])
print('Second hobby:', details_dictionary['hobbies'][1])

