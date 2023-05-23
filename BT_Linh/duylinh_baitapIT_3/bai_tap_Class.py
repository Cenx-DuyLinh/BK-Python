class LoggingDatabase:
    def __init__(self,input_number,data):
        self.data = data
        self.input_number = input_number
    def get(self):
        print(self.data)
    def create_file(self):
        input_string = str(self.input_number)
        a_buffer = '.txt'
        input_string = input_string + a_buffer
        with open(input_string, 'w') as f:
            f.write(self.data)
#----------------------------------------------------------------
def get_properties():
    i=1
    while i>0:
        try :
            properties_want_to_run = int(input("Please choose properties: \n 1: Save data \n 2: Get data \n 3: Create file \n 4: End \n"))
        except :
            i = i + 1
            print("Please choose again!")
            continue
        else:
            if properties_want_to_run not in range(0,5,1):
                print ("Please choose again !")
                continue
            else: 
                return properties_want_to_run
#----------------------------------------------------------------
def get_number_for_properties_2_and_3(input_count):
    i=1
    while i>0:
        try :
            output = int(input())
        except :
            i = i + 1
            print("Please choose again!")
            continue
        else:
            if output not in range(0,input_count+1,1):
                print ("Please choose again !")
                continue
            else: 
                return output
#----------------------------------------------------------------
def RUN():
    i = 1
    input_count = 0
    data_slot={}
    while i>0:
        properties_want_to_run = get_properties()
        if properties_want_to_run == 4:
            break
        elif properties_want_to_run == 1:
            input_count = input_count + 1
            data_input = input("Please type the data you want to save: ")
            data_slot["data_".format(input_count)] = LoggingDatabase(input_count,data_input)
        elif properties_want_to_run == 2:
            if input_count == 0 :
                print("No file has been save yet")
                continue
            print('Please choose the save file you want to get: ')
            i2 = 1
            while i2 <= input_count:
                print('Save number ',i2)
                i2 = i2 + 1
            file_choose = get_number_for_properties_2_and_3(input_count)
            data_slot["data_".format(file_choose)].get()
        elif properties_want_to_run == 3:
            if input_count == 0 :
                print("No file has been save yet")
                continue
            print('Please choose the save file you want to create: ')
            i2 = 1
            while i2 <= input_count:
                print('Save number ',i2)
                i2 = i2 + 1
            file_choose = get_number_for_properties_2_and_3(input_count)
            data_slot["data_".format(file_choose)].create_file()


if __name__ == "__main__":
        RUN()

