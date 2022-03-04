over18 = input("Are you over 18 (True/False): ")

over18 = bool(over18)

#  A simple if construct can be reduced to 1 line
#  if over18 == True: print('you are eligible to vote')
if over18: print('you are eligible to vote')

#  The ternary operator can be used to reduce a simple if else to a single line of python code
x , y = 10 , 15

# if x < y:
#     smaller = x
# else:
#     smaller = y

smaller = x if x < y else y 

print('smaller', smaller )