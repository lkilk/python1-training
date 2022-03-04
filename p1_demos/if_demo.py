my_num = input("Enter a number: ")
my_num = int(my_num) 
#  Could refactor to 1 line of code : my_num = int ( input("Enter a number: ") )

if my_num < 0:
    print("In the if block") 
    print(my_num, "< 0")

elif my_num == 0:
    print("In the first elif block") 
    print(my_num, "= 0")

elif my_num > 0 and my_num <= 10:
    print("In the first elif block") 
    print(my_num, "> 0 and <= 10")
    
else:
    print("\nIn the else block") 
    print(my_num, "> 10")

print("\n Outside the if construct")
