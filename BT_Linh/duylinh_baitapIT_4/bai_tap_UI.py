def RUN():
    import tkinter as tk
    from threading import Thread
    import time
    import random

    def update_infoview(infoview_object,time):
        while True:
            object_value_buffer = infoview_object.get()
            new_value = object_value_buffer + random.randint(1,4)
            infoview_object.set(new_value)
            time.sleep(time)
        

    #Create the window
    window = tk.Tk()
    window.geometry('600x500')

    #Create the class
    class infoview:
        def __init__(self,name,window,row, column) ->None:
            self.name = name     
            self.row = row
            self.window=window
            self.column=column
            self.value=0
            #Create the UI object
            self.label_name= tk.Label(self.window, text = self.name, borderwidth=1, relief= 'solid', width=10, height=2 )
            self.label_value= tk.Label(self.window, text=self.value, borderwidth=1, relief= 'ridge' )
            #Position the object
            self.label_name.grid(row=self.row, column=self.column, padx = 60, pady = 20)
            self.label_value.grid(row=self.row + 1, column=self.column, padx = 60, pady = 20)
        def get(self):
            return self.value
        def set(self,newvalue):
            self.value= newvalue
            self.label_value.config(text=self.value)

    object_pitch = infoview("Pitch",window,1,1)
    object_yaw = infoview ("Yaw",window,1,2)
    object_roll = infoview('Roll',window,1,3)

    #Update thread
    thread = Thread(target= update_infoview, args = (object_pitch,1, ))
    thread2 = Thread(target= update_infoview, args = (object_yaw,0.5, ))
    thread3 = Thread(target= update_infoview, args = (object_roll,2, ))

    thread.start()
    thread2.start()
    thread3.start()
    
    #Run the UI
    window.mainloop()

if __name__ == '__main__':
    RUN()

