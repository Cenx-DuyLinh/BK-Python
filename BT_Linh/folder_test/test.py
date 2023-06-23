def RUN():
    from InputComponentAbstract import InputComponentAbstract
    import tkinter as tk
    from tkinter import messagebox
    class GPSInputInfor:
        def __init__(self, latitude, longitude, altitude, latitude_flag, longitude_flag, altitude_flag) -> None:
            self.latitude_flag = latitude_flag
            self.longitude_flag = longitude_flag
            self.altitude_flag = altitude_flag


            # Set None values if the corresponding flag is False
            self.latitude = None if not self.latitude_flag or (self.latitude_flag and (latitude == '' or latitude is None)) else latitude
            self.longitude = None if not self.longitude_flag or (self.longitude_flag and (longitude == '' or longitude is None)) else longitude
            self.altitude = None if not self.altitude_flag or (self.altitude_flag and (altitude == '' or altitude is None)) else altitude

            # Check if altitude is negative and set it to None
            if self.altitude is not None and float(self.altitude) < 0:
                messagebox.showerror("Invalid value", "The input altitude cannot be negative!")
                self.altitude = None

            # Try to convert latitude, longitude and altitude to float
            try:
                self.latitude = None if self.latitude is None else float(self.latitude)
                self.longitude = None if self.longitude is None else float(self.longitude)
                self.altitude = None if self.altitude is None else float(self.altitude)
            except ValueError:
                messagebox.showerror("Invalid value", "Invalid input, please enter a numerical value for latitude, longitude and altitude!")

        def print_test(self):
            print(f"{self.latitude}, {self.longitude}, {self.altitude}")

    class InputInforGPSComponent(InputComponentAbstract):
        def __init__(self,__window,__name,__row,__column) -> None:
            self.name = __name
            self.window = __window
            self.row = __row
            self.column = __column

            def focus_next(event):
                event.widget.tk_focusNext().focus()
                return "break"       
            #Create UI
            self.frame = tk.Frame(self.window,width=400, height=300,borderwidth=1, relief='solid')
            self.frame.grid_propagate(False)
            self.frame.grid(row=self.row, column=self.column, padx = 20, pady=20)

            self.height_component = 1

            self.label_title = tk.Label(self.frame, text=self.name, borderwidth=1, width = 10, height= 2, relief='solid')

            self.entry_latitude = tk.Entry(self.frame)
            self.entry_longitude = tk.Entry(self.frame)
            self.entry_altitude = tk.Entry(self.frame)

            self.entry_latitude.delete(0, tk.END)
            self.entry_latitude.config(state="disabled")

            self.entry_longitude.delete(0, tk.END)
            self.entry_longitude.config(state="disabled")

            self.entry_altitude.delete(0, tk.END)
            self.entry_altitude.config(state="disabled")

            def toggle_entry_latitude():
                if self.checkbutton_latitude_var.get():
                    self.entry_latitude.config(state="normal")
                else:
                    self.entry_latitude.delete(0, tk.END)
                    self.entry_latitude.config(state="disabled")
            def toggle_entry_longitude():
                if self.checkbutton_longitude_var.get():
                    self.entry_longitude.config(state="normal")
                else:
                    self.entry_longitude.delete(0, tk.END)
                    self.entry_longitude.config(state="disabled")
            def toggle_entry_altitude():
                if self.checkbutton_altitude_var.get():
                    self.entry_altitude.config(state="normal")
                else:
                    self.entry_altitude.delete(0, tk.END)
                    self.entry_altitude.config(state="disabled")

            self.checkbutton_latitude_var = tk.BooleanVar()
            self.checkbutton_longitude_var = tk.BooleanVar()
            self.checkbutton_altitude_var = tk.BooleanVar()

            self.checkbutton_latitude = tk.Checkbutton(self.frame, variable =  self.checkbutton_latitude_var, text = 'Latitude', borderwidth=1, width=20, height=self.height_component,command=toggle_entry_latitude)
            self.checkbutton_longitude = tk.Checkbutton(self.frame, variable = self.checkbutton_longitude_var, text = 'Longitude', borderwidth=1, width=20, height=self.height_component,command=toggle_entry_longitude)
            self.checkbutton_altitude = tk.Checkbutton(self.frame, variable = self.checkbutton_altitude_var, text = 'Altitude', borderwidth=1, width=20, height=self.height_component,command=toggle_entry_altitude)

            self.button_submit = tk.Button(self.frame, text = 'Submit', borderwidth=1, width=10, height=self.height_component, command=self.DefineTypeOfGetData)


            #Positionining Component
            self.padx = 10
            self.pady = 10
            self.checkbutton_column = 0
            self.entry_column = 1

            self.label_title.grid(row=0,column=0,padx=self.padx,pady=self.pady, columnspan=2)


            self.checkbutton_latitude.grid(row=1,column=self.checkbutton_column,padx=self.padx,pady=self.pady)
            self.checkbutton_longitude.grid(row=2,column=self.checkbutton_column,padx=self.padx,pady=self.pady)
            self.checkbutton_altitude.grid(row=3,column=self.checkbutton_column,padx=self.padx,pady=self.pady)

            self.entry_latitude.grid(row=1,column=self.entry_column,padx=self.padx,pady=self.pady)
            self.entry_longitude.grid(row=2,column=self.entry_column,padx=self.padx,pady=self.pady)
            self.entry_altitude.grid(row=3,column=self.entry_column,padx=self.padx,pady=self.pady)     

            self.button_submit.grid(row=4,column=0,padx=self.padx,pady=50,columnspan=2)

            # bind the <Return> event to the callback function for all the text boxes
            self.entry_altitude.bind("<Return>", focus_next)
            self.entry_latitude.bind("<Return>", focus_next)
            self.entry_longitude.bind("<Return>", focus_next)

            #Change column weight
            self.frame.columnconfigure(0, weight=1)
            self.frame.columnconfigure(1, weight=1)

        def DefineTypeOfGetData(self):
            latitude = self.entry_latitude.get()
            longitude = self.entry_longitude.get()
            altitude = self.entry_altitude.get()
            latitude_flag = self.checkbutton_latitude_var.get()
            longitude_flag = self.checkbutton_longitude_var.get()
            altitude_flag = self.checkbutton_altitude_var.get()
            GPSInforObject = GPSInputInfor(latitude,longitude,altitude,latitude_flag, longitude_flag, altitude_flag)
            return GPSInforObject


    window = tk.Tk()

    test = InputInforGPSComponent(window, 'GPS Input', 0, 0)

    window.mainloop()

if __name__ == '__main__':
    RUN()
