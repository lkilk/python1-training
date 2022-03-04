def get_number():
    num = float(input('Enter a number: '))
    print(num)
    return num

while True:
    try: 
        get_number()
        break
    except:
        print("Not a number, try again")



