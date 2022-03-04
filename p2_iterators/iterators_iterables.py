# an iterable needs to implement __iter__(): which reterns an iterator

# Iterator should implement __next__ which returns the next element or a stop iteration exception when it reaches the end of the iterable
# the iterator must retain state information

class MyIterable:

    def __init__(self, number):
        self.max = number
        self.numbers = list(range(number))

    def __iter__(self):
        return MyIterator(self.numbers)

class MyIterator:

    def __init__(self, container):
        self.current_index = -1
        self.container = container

    def __next__(self):
        self.current_index += 1
        if self.current_index >= len(self.container):
            raise StopIteration('The end is nigh')
        else:
            return self.container[self.current_index]


iterable = MyIterable(10)
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
