# decorators

def dec(func):
    
    def inner(a,b):
        print(func.__name__)
        if b != 0:
            return func(a,b)
        else:
            raise ValueError("second argument cannot be 0")
    return inner


@dec
def div(a,b):
    return a / b
@dec
def mult(a,b):
    return a * b 


print(div(1,2)) # dec(div)(a,b) a call to the div functionn now also includes a call to the decorator - dec - validitity can be added by using a decorator without changing the exisitng functions
print(mult(1,0))

