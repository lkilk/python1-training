filename = 'students.dat'
file_ref = open(filename,"w")
delegates = ['Harry\n', 'Ron\n', 'Hermione\n', 'Albus\n', 'Tom\n', 'Severus\n']
file_ref.writelines(delegates)
file_ref.close()

file_read_ref = open(filename , "r")

results = []

for line in file_read_ref:
    name = line.strip('\n')
    grade = input(f'Enter the grade for {name}: ')
    results.append((name, grade))

file_read_ref.close()

newfilename = 'studentgrades.dat'
file_write_ref = open(newfilename,"w")
print(results)

for name, grade in results:
    file_write_ref.write(f"{name}, {grade}\n")

