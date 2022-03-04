from decimal import DivisionByZero

try:

    filename = input("Enter the file to process: ")
    nrofmonth = int(input("Enter numeric day of the month: ") )
    if not 1 <= nrofmonth <= 31:
        raise Exception('day must be between 1 and 31')

    num1 = input("Enter first number: ")
    num1 = int(num1)

    num2 = int( input("Enter second number: ") )

    fh = open(filename , 'r')

    for line in fh:
        pass

    import kf_my_functions as kff

    kff.divide_nums(num1 , num2)

except (FileNotFoundError,FileExistsError) as fne:
    print("File not found:" , fne )
except DivisionByZero as dze:
    print("Division by zero exception:" , dze )
except Exception as err:
    print("\nA runtime exception has occurred", err ) 
else:
    print("This will execute only when no exception is raised in the try block")
finally:
    print("This will execute if an exception is raised in the try block or not")
