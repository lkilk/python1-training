
class A: 
    
    def __init__(self):
        pass

    def greetings(self):
        print("Hello from A")

class B:
    
    msg = "Messgae from B"
    def __init__(self):
        pass

    def greetings(self):
        print("Hello from B")

    def goobye(self):
        print("Goodbye from B")

    def print_msg(self):
        print(self.msg)

class C(A):
    
    msg = "Messgae from C"
    
    def __init__(self):
        pass

    def goodbye(self):
        print('Goodbye from C')

class D(C,B):

    def __init__(self):
        pass
d = D()

d.greetings()
d.print_msg()


