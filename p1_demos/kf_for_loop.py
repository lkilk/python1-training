namesL = ["Lei",'Andrew','Marc','Catherine','Ian']

for letter in 'Hello':
    print(letter)

for name in namesL:
    print("Name:" , name )

#  for idx in range(5):
for idx in range( len(namesL) ):
    print("Idx:" , idx , "Name:" , namesL[idx] )

for item in enumerate( namesL ):
    print('Item:' , item)

for item in enumerate( namesL ):
    print(item[0], item[1])

for idx, name in enumerate( namesL ):
    print(f"Idx: {idx} Name: {name}" )
