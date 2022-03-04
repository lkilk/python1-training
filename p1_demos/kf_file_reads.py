filename = "names.txt"

file_ref = open(filename , "r")

fileAsString = file_ref.read() # reads the whole file into a string
print("File position after read():", file_ref.tell())

file_ref.seek(0,0) # Go to beginning of file and offset by 0 characters
linesAsList = file_ref.readlines()

# file_ref.readline() # reads up to the end of the line and returns the resultant string
print('linesAsList:' , linesAsList)

file_ref.seek(0,0)

for line in file_ref:
    if line.lower().startswith('ian'):
        print('Which Ian -' , line.rstrip())
    else:
        print('Not Ian -' , line , end="")

file_ref.close()