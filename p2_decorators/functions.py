#functions 1st objects
## 1. assignable 
## 2. pass as arguments to other functions
## 3. return them from other functions 

# a high level function takes a function as an argument

def div(a,b):
    return a / b

def mult(a,b):
    return a * b 

## assigning a function 

# func = div
# print(func(3,5))

# func = mult
# print(func(3,4))

# 2. pass as argument 

def executer(func, a, b):
    print(f"Executing {func.__name__}")
    return func(a, b)

print(executer(div, 3, 5))
print(executer(mult, 3, 5))

# 3. returning a function 

def return_func(func):
    print(f"You have passed me {func.__name__}")
    return func

func = return_func(div)
print(func(3,5))