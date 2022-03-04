# newspaper = input("Enter a newspaper: ")
# price = float( input("Enter a price: ") )
newspaper = "The Daily Bugle"
price = 2.50

formatted_string = f'\nNewspapers: {newspaper} - Price: {price}'
formatted_string1 = f'\nNewspaper: {newspaper:20} - Price: {price:6}'
formatted_string2 = f'\nNewspaper: {newspaper:^20s} - Price: {price:<6.2f}'

print(formatted_string)
print(formatted_string1)
print(formatted_string2)
