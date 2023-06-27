import tkinter as tk
from tkinter import font
class DroneControlApp:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Drone Control App')
        self.frame_transit = tk.Frame(self.window)
        self.frame_search = tk.Frame(self.window)
        
        custom_font = font.Font(family="Tahoma", size=30, weight="bold", slant="italic")
        self.label_title = tk.Label(master=self.window, text= 'Drone Control',font=custom_font)
        self.label_title.grid(row=0,column= 0, columnspan=2)

        #Frame transit
        button_width = 10
        button_heigth = 2
        custom_font_label = font.Font(underline=True)
        self.label_transit = tk.Label(master=self.frame_transit, text='Transit Operation', font = custom_font_label)
        self.button_arm = tk.Button(master=self.frame_transit, text='Arm & Takeoff',width=button_width,height=button_heigth,command=None)
        self.button_setspeed = tk.Button(master=self.frame_transit, text='Set Speed',width=button_width,height=button_heigth,command=None)
        self.button_123 = tk.Button(master=self.frame_transit, text='Enter transit 1-2-3',width=button_width,height=button_heigth,command=None)
        self.button_321 = tk.Button(master=self.frame_transit, text='Exit transit 3-2-1',width=button_width,height=button_heigth,command=None)
        
        self.entry_setspeed 
        self.entry_arm 

        self.window.mainloop()

object = DroneControlApp()