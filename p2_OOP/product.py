# Class
## Attributes (fname, sname, acc_no, ) 
## every instance of the class has these attributes but they have unquie values 
### Methods : accessor methods can be used to access & change the atributes 

# Enity: Product 
## Attribtes: cost, desc, origin, disc_rate
## Methods: bulk_cost(quanity) 

class Product: 

    def __init__(self, desc, price, origin, disc_rate): ## self - equivilant of this in Java. Initializes attributes
        self.desc = desc
        self.price = price
        self.origin = origin
        self.disc_rate = disc_rate

    def bulk_cost(self, quanity):
        cost = self.price * quanity
        discount = cost * self.disc_rate / 100.0
        discounted_price = cost - discount
        return discounted_price

product_1 = Product('Tea', 1.99, 'Kenya', 10)
product_2 = Product('Coffee', 3.49, 'Mexico', 15)
product_3 = Product('Orange Juice', 5.99, 'Spain', 8)

product_2.quality = "Great" # attaching an attribute on the fly like this only adds it to the instance not the class

print(f"Product all attributes {product_1.__dict__}")
print(f"Product all attributes {product_2.__dict__}")
print(f"Product all attributes {product_3.__dict__}")

# Product(desc, cost, origin, disc_rate)
# Product.__new__() # create an object withot attributes, returns a reference (say self)
# Product.__init__(self, desc, cost, origin, disc_rate) #


print(f"Bulk cost of {product_1.desc} is £{product_1.bulk_cost(100)}")

product_1.bulk_cost(100) # Product.bulk_cost(product_1, 100) - this is what happens under the hood. 

print(f"100 units of tea cost {Product.bulk_cost(product_1, 100)}") 

