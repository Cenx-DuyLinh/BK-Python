# Print all file name in current folder
import os

print('List of files in current folder:')
# Get all name in current folder
for name in os.listdir():
    if os.path.isfile(name): # Check if 'name' if file or folder
        print(name) # Print file name