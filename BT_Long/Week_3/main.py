# Week 3: Write a program to create a class that content 3 methods
# 1. Save: save the user input entries and time at that moment( Last edited time) 
# 2. Get: Print out the log entries and time of called object
# 3. Create: Create an txt file on local directory
import os
from datetime import datetime as dt 

class LoggingDatabase:
    def __init__(self, log_name):
        self.log_name = log_name
        self.log_entries = str()
        self.log_dates_and_times = str()
        
    def save(self, log_entry): # Method 1
        self.log_entries = log_entry
        unconverted_date_and_time = dt.now()
        self.log_dates_and_times = unconverted_date_and_time.strftime("[%d-%m-%y %H:%M:%S] ")
        
    def get(self): # Method 2
        print(self.log_dates_and_times + self.log_entries)
        return self.log_dates_and_times + self.log_entries

    def create(self): # Method 3
        temp_buffer = ".txt"
        with open(self.log_name + temp_buffer, "w", encoding="utf-8") as file:
            content = self.log_dates_and_times + self.log_entries
            file.write(content)
        return print('File successfully created')
        


def RUN(): 
     log_db = LoggingDatabase(str(input('Input new log name: '))) # Note: Log with same name will be overwrite
     log_db.save(str(input('Input log entries: '))) # Input content to store in created log
     log_db.get()
     log_db.create()

if __name__ == "__main__":
        RUN()