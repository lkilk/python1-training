# a generator is like a function but it yields something rather than returning it 
# a generator is also an iterator so we can call next on it 

def numbers(n):
    yield n 
    print("after 1st yield")
    n -= 1
    yield n 
    print("after 2nd yield")
    n -= 1
    yield n 
    print("after 3rd yield")
   


my_gen = numbers(7) 

print(type(my_gen))

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
