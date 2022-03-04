#  Option 1 - import the full module
# import kf_my_functions
# kf_my_functions.multiply_nums(7,4)

# Option 2 - import full module with alias
# import kf_my_functions as kmf
# kmf.multiply_nums(7,4)

# Option 3 - import individual functions/classes etc from the module
# from kf_my_functions import multiply_nums , divide_nums
# multiply_nums(7,4)

# Option 4 - import all individual functions/classes etc from the module
# from kf_my_functions import *
# multiply_nums(7,4)

# print(dir()) # Using this to see what has been imported into the namespace

import sys
file_to_add = '/home/user1/'
# sys.path.append(file_to_add) # sys.path will be used to find an imported module 
print('System path used to find modules:\n',sys.path) 

import kf_my_functions as kmf
#  To add directories to the sys.path more permanently you can defnie the PYTHONPATH
# environment variable 

# You can view the PYTHONPATH setting in your python code
import os
print('\nPYTHONPATH:' , os.environ['PYTHONPATH'])