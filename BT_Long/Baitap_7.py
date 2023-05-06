# Check if file exist in current folder
import os

# Input file's name to check
name = input('Input file name: ')

# Check and print result
if os.path.exists(name):
    print(name ,'exists in current folder')
else:
    print(name ,'does not exists in current folder')