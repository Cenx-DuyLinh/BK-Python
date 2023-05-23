def RUN():
    import tkinter as tk
    from threading import Thread
    import time
    import random
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import pandas as pd

    #Create the window
    window = tk.Tk()
    window.geometry('600x500')

    data_test = {'x_axis':[0,1,2,3,4,5],'y_axis':[2,4,5,2,4,7]}
    data_frame = pd.DataFrame(data_test)
    figure_buffer = plt.Figure(figsize=(5,4),dpi=100)
    figure_plot = figure_buffer.add_subplot(1,1,1)
    #Place figure on main window
    line = FigureCanvasTkAgg(figure_buffer,window)
    # get_tk_widget
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) #position the graph
    # Meant for actual dates - groups unemployment rates by year and adds them up
    data_frame.plot(kind='line', legend=True, ax=figure_plot, color='r', marker='o', fontsize=10)

    #Run the UI
    window.mainloop()

if __name__ == '__main__':
    RUN()

