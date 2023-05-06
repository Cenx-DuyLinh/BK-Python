# Print path of current running file
import os 

# Get and print file name
name = os.path.basename(__file__)
print('Name of current file: ',name)

# Get and print path
path = os.path.dirname(__file__)
print('Path of current file: ',path)