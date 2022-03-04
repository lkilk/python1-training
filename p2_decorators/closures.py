
def div(a,b):
    return a / b

def mult(a,b):
    return a * b 


def delayed(func):
    msg = "executing a delayed function"
    # defining inner function
    def inner(a,b):
        print(msg)
        return func(a,b) # passed function called

    return inner # inner function being returned

func = delayed(div)
print(func.__name__)

print(func(15,3))
