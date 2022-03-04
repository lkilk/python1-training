''' Create a script that does the following:
1) Displays a menu that gives the user the following choices
   1) Process a csv file
   2) Process a json file
   3) Multiple 2 numbers
   4) Divide 2 numbers
   5) Exit the program

On choosing an option, display the result then ask the user to hit return to contine.
On hitting return clear the screen and redisplay the menu options

'''
import csv
import json
import os

menu_display =  '''
\nChoose from 1 of the following options:\n
1) Process a csv file
2) Process a json file
3) Multiply 2 numbers
4) Divide 2 numbers
5) Exit the program\n
'''

while True:
    if os.name == 'nt':
        _=os.system('cls')
    else:
        _=os.system('clear')

    choice = input( menu_display)
    
    if choice == '1':
        filename = input('\nEnter the csv file to process: ')
        fhandler = open(filename,'r')
        csvReader = csv.reader(filename)
    elif choice == '2':
        filename = input('\nEnter the json file to process: ')
        fhandler = open(filename,'r')
        jsonDict = json.load(filename)
    elif choice =='3':
        num1 = int( input ( '\nEnter first number: ') )
        num2 = int (input ( 'Enter second number: ') )
        print(f'{num1} * {num2} = {num1 * num2}')
    elif choice =='4':
        num1 = int( input ( '\nEnter first number: ') )
        num2 = int( input ( 'Enter second number: ') )
        print(f'{num1} / {num2} = {num1 / num2:.2f}')
    elif choice == '5':
        print('\nexiting the program')
        break
    else:
        print('\nInvalid option, try again')

    input('\nHit return to continue ')