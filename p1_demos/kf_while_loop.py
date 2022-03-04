loopcnt = 1

while True:
#  while loopcnt <= 20:
    print('loopcnt:' , loopcnt)
    loopcnt += 1
    if loopcnt > 10:
        print('Breaking out of the loop prematurely')
        break
else:
    print("Loop has terminated/ended naturally")

print('\nAfter the while loop')