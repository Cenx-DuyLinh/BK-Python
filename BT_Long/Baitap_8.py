# Week 1_Check if file exist in current folder and delete
# Week 2_Add functions, parameters check using Try, Exception and Flags

import os
import sys

# Define function to get file name and return flag
def get_file_name():
    try:
        file_name = input('Input file name to delete: ')
        return file_name 
    except:
        print('Error input')
        sys.exit() # Incase of error, return message and stop the program

# Define function to check if file exists and return flag
def check_if_file_exists(file_name):
    try:
        return os.path.exists(file_name) 
    except:
        return False # return False if there's an error

# Define function to delete file if exists and return flag
def delete_file(file_name):
    try:
        os.remove(file_name)
        return True # return True if the file is successfully deleted
    except:
        return False # return False if there's an error

# Excecute function
file_name = get_file_name()
if check_if_file_exists(file_name):
    if delete_file(file_name):
        print("File deleted successfully.")
    else:
        print("Error deleting file.")
else:
    print("File does not exist.") 
