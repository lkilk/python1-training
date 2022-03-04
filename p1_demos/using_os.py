import os
import shutil

cwd = os.getcwd()
print(f'Current working directory: {cwd}')

filesInCwd = os.listdir()

print(f'Files in {os.getcwd()}\n')
print(filesInCwd)

print(f"Number of files in {cwd}: {len(filesInCwd)}")
# Create a sub directory
subdir = "functions"

if subdir not in os.listdir():
    os.mkdir(subdir)

# Change directory
os.chdir(subdir)

print(f'\nCurrent working directory: {os.getcwd()}')

shutil.copy('/home/user1/pyp/kf_my_functions.py','.')

