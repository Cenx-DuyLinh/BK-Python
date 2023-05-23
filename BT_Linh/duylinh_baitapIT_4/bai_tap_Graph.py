def RUN():
    import tkinter as tk
    from threading import Thread
    import time
    import random
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    #Create the window
    window = tk.Tk()
    window.geometry('600x500')

    
    figure_buffer = plt.Figure(figsize=(5,4),dpi=100)
    figure_plot = figure_buffer.add_subplot(1,1,1)
    #Place figure on main window
    line = FigureCanvasTkAgg(figure_buffer,window)
    # get_tk_widget
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    # Meant for actual dates - groups unemployment rates by year and adds them up


    #Create the class
    class graph:
        def __init__(self,name) -> None:
            self.name = name

    #Run the UI
    window.mainloop()

if __name__ == '__main__':
    RUN()

