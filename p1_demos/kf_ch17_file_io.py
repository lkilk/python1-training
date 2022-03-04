with open("students.dat") as file:
    results = []
    for name in file:
        
        name = name.rstrip()
        grade = input(f"Enter grade for {name}: ")
        results.append((name, grade))
        input("Hit return to continue: ")

with open("studentGrades.dat", "w") as file:
    for name, grade in results:
        file.write(f"{name},{grade}\n")

import os
os.system('cat studentGrades.dat')
