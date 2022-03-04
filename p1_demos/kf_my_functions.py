# num1 = 10 # This variable has global scope
# num2 = 12

def add_nums():
    print("Executing the add_nums function")
    result = num1 + num2 # the result variable has local scope i.e. function access only
    print(f'{num1} + {num2} = {result}')

def multiply_nums( p_num1 : int, p_num2 : int = 1 ): # the type annotation is just a hint
    print("Executing the multiply_nums function")
    result = p_num1 * p_num2 # the result variable has local scope i.e. function access only
    print(f'{p_num1} * {p_num2} = {result}')

def divide_nums( p_num1 : int, p_num2 : int ) -> float: 
    print("Executing the divide_nums function")
    result = p_num1 / p_num2 
    return result # This will cause the function to exit and will pass back a value

def get_summary( num_list : list ) -> dict:
    num_dict = {}
    num_dict['elements'] = num_list
    num_dict['sum'] = sum(num_list)
    count = len(num_list)
    num_dict['count'] = count 
    num_dict['mean'] = sum(num_list) / count
    return num_dict

# add_nums()
# multiply_nums(num1 , num2 ) 
# multiply_nums(5 , 6 ) 
# multiply_nums(5) 

# gResult = divide_nums( num1 , num2 )

# print(f'{num1} / {num2} = {gResult}')
# print(f'{num1} / {num2} = {divide_nums( num1 , num2 )}')

# gNum_list = [34,12,67,99,21,12]

# print( get_summary (gNum_list ) )
