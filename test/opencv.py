import tkinter as tk
class DroneControlApp:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Drone Control App')
        self.frame_transit = tk.Frame(self.window)
        self.frame_search = tk.Frame(self.window)
        
        self.label_title = tk.Label(master=self.window, text= 'Drone Control')
        self.label_title.grid(row=0,column= 0, columnspan=2)

        #Frame transit
        self.label_transit

        self.window.mainloop()