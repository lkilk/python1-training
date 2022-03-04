import re
filename = "natinsnrs.txt"
file_ref = open(filename , "r")

nino_pattern = "^[A-Z]{2}[0-9]{6}[A-Z]$"

invalid_ninos = 'bad_nums.dat'
file_write_ref = open(invalid_ninos,"w")

for nino in file_ref:
    ok = re.match(nino_pattern , nino)
    if ok:
        print(nino)
    else:
        file_write_ref.write(nino)
         
        
file_write_ref.close
