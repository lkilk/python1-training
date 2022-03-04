name = 'Liam'
age = 31
job = input('Enter a job title: ')

print( name, age, job ) 
print( '\nName:', name , '\nAge:', age , '\nJob:', job , sep='\t' ) 
#  Default seperator is a space, can ammend using sep=
#  \n = newline \t = tab 

print(f'Name: {name} \n Age: {age} \n Job: {job}')
