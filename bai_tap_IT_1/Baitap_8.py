# Check if file exist in current folder and delete
import os

# Input file's name to check
name = input('Input file name: ')

# Check and delete option
if os.path.exists(name):
    print(name ,'exists in current folder')
    print('Do you want to delete ',name,'?')
    flag = input('[y/n]: ') # Ask user whether delete or not
    if flag == 'y':
        os.remove(name)
        print('File removed') # Delete command
    elif flag == 'n':
        print('End task.')
    else:
        print('Inapporiate input -> End task.')
else:
    print(name ,'does not exists in current folder')