## Iterators and Generators

## iterators and iterables 
## an iterator traverses(iterates over) an iterable 

# an iterator needs to return (when asked) an iterator to itself
## iterable : implements __iter(): iterator 

## the iterable returns an interator 

## a list is a iterable 
lst =[1,2,3,4,5,6,7,8,9]

lst_iterator = lst.__iter__()
lst_iterator_2 = iter(lst) # this is doing the same as above but the better way to do it, creating an iterator that will traverse through teh iterable list. 
print(type(lst_iterator)) # type returned is a list iterator 
print(lst_iterator.__next__()) # returns 1
print(lst_iterator.__next__()) # returns 2, 

print(next(lst_iterator_2)) # again how to do the same as above without using the dunder methods 
print(next(lst_iterator_2))