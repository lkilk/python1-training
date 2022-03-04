def get_number():
    while True:
        num = input('Enter a number: ')
        try:
            num = float(num)
            return num
        except:
            print('Not a number, try again')

num = get_number()
print(num)