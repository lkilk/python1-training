class Address: 

    BEST_ADDRESS = '10 Mayfair'

    def __init__(self, door, street, city):
            self.street = street
            self.door = door
            self.city = city 

    @classmethod
    def address_from_str(cls, addr_str):
        door, street, city = addr_str.split(' ')
        return Address(door, street, city)

    def __str__(self):
        return f"{self.door} {self.street} {self.city}"

    @staticmethod
    def prime_minister_office():
        return "10 Downing Street"


# gov_add = Address(10, 'Downing Street', 'London')
# gov_add_2 = Address.address_from_str('10 DowningStreet London')

# print(gov_add)
# print(gov_add_2)

print(Address.prime_minister_office())