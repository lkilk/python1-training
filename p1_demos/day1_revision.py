# 1) Create a variable my_int that stores any integer value
my_int = 2

# 2) Create a variable called my_float that stores any float value.
my_float = 2.12

# 3) Create a variable called my_string that stores any string value.
my_string = "This is my string"

# 4) Display the length of the variable my_string.
print(len(my_string))

# 5) Display the 1st character stored my_string.
print(my_string[0])

# 6) Create a list variable called my_list that contains 4 elements 
#    - these elements can be of any datatype.
my_list = ["Apples","Oranges","Pears","Plums"]

# 7) Use an if statement to check if a value exists in the my_list variable.
if "Apples" in my_list:
    print("found it!")
else:
    print("not there!")

# 8) Create a tuple variable called my_tuple from the my_list variable 
my_tuple = tuple(my_list)
print(my_tuple)

# 9) Create a dictionary variable called person_dict that will store 
#    the following information
#    i)   first name ii)  last name iii) age iv)  address

person_dict = {"first_name":"Liam", "last_name":"Kilkenny", "age":31, "address":"12 Electric Avenue"}
# 10) Use a for loop to display each element in the my_list variable to the terminal
for fruit in my_list:
    print(fruit)

# 11) Use a for loop to display each element and it's index in the my_list variable to 
#     the terminal
for idx, fruit in enumerate(my_list):
    print(idx, fruit) 
