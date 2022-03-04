filename = "names.txt"

file_ref = open(filename,"w") # other modes "r (read), "a" (append) , "w+" (Write and read) 
print("Character Position in file after open:", file_ref.tell())

file_ref.write("Ian Kilminister\n")
print("Characters written:", file_ref.write("Ian McCullough\n") )

print("Character Position in file after writes:", file_ref.tell())

ians_in_rock = ["Ian Brown\n","Ian Broudie\n","Ian Astbury\n","Ian Paice\n","Janis Ian\n"]

file_ref.writelines(ians_in_rock)

file_ref.close()