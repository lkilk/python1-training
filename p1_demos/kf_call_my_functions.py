from my_functions import multiply_nums , divide_nums , get_summary

num1 = 10 # This variable has global scope
num2 = 12

multiply_nums(5 , 6 ) 
gResult = divide_nums( num1 , num2 )

print(f'{num1} / {num2} = {gResult}')
print(f'{num1} / {num2} = {divide_nums( num1 , num2 )}')

gNum_list = [34,12,67,99,21,12]

print( get_summary (gNum_list ) )
