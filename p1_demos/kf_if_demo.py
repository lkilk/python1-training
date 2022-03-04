#  my_num = int ( input("Enter a number: ") )
my_num = input("Enter a number: ")
my_num = int ( my_num )

if my_num < 0:
    print("\nIn the if block")
    print(my_num, "< 0")

elif my_num == 0:
    print("\nIn the first elif block")
    print(my_num, "== 0")

elif my_num > 0 and my_num <= 10:
    print("\nIn the second elif block")
    print(my_num, "> 0 and <= 10")
    
else:
    print("\nIn the else block")
    print(my_num, "> 10")

print("\nOutside the if construct")