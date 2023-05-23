import tkinter as tk
from threading import Thread
from time import sleep

def button_click():
    print("Button clicked!")
#define sub thead handler with inforview agrument
def update_inforview(inforviewObject):
    while True:
        CurrentValueBuffer=inforviewObject. get()
        inforviewObject.set(CurrentValueBuffer+1) 
        time.sleep(1)
    
    
def RUN():
    # Create the main window
    window = tk.Tk()
    window.title("Example GUI")

    # Create a button
    button = tk.Button(window, text="Click me!", command=button_click)
    button.grid(row=0, column=0, padx=50, pady=10)  # Set the position using grid()

    PitchInforObject= inforview("Pitch",window,1,0)
    RollInforViewObject=inforview("Roll",window,1,2)
    thread = Thread(target = update_inforview, args = (PitchInforObject, ))
    thread.start()
    window.mainloop()

    print("Somthings")

class inforview:
    def __init__(self,name,window,row,column) -> None:
        self.name = name
        self.value = 0
        self.window = window
        label = tk.Label(window, text=self.name)
        label.grid(row=row, column=column, padx=10, pady=10)  # Set the position using grid()
        self.label2 = tk.Label(window, text= self.value)
        self.label2.grid(row=row+1, column=column, padx=10, pady=10)  # Set the position using grid()
        pass
    def set(self,newvalue):
        self.value = newvalue
        self.label2.config(text= self.value)
    def get(self):
        return self.value
if __name__ == "__main__":
        RUN()