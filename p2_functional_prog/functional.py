from functools import reduce 


# map, reduce, filter

# 1. map(func, seq_data) : func: one ---> one :  the function takes one unit of data, takes one variable and returns one variable 

pounds = [105, 67, 99, 50, 60, 70, 80, 90, 100, 40, 20, 30, 10]

# def convert(a):
#     return a * 1.2 

# dollars = list(map(convert, pounds))
# print(dollars)

# for d in map(convert, pounds):
#     print(d)


# 2. reduce(func, data) : func: two ---> one : takes 2 pieces of data and returns one 

# def re(a,b):
#     return(min(a,b))

# lowestnum = reduce(re, pounds)
# print(lowestnum)

lowest = reduce(lambda a,b: a if a < b else b, pounds)
print(lowest)

# 3. filter(func, data) : func: one ---> bool : takes 1, returns true or false


# def fl(p):
#     return p < 50

filtered = list(filter(lambda num: num < 50, pounds)) # we can use a lambda instead of defining a function which we only use once
print(filtered)
    
