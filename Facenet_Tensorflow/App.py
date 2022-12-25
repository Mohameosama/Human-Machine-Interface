import tkinter as tk
import os
from imageCollectorScript import FaceCollector
# creates a Tk() object
master = tk.Tk()

# sets the geometry of main
# root window
master.geometry("500x500")


# function to open a new window
# on a button click
def openNewWindow():
    

    # Toplevel object which will
    # be treated as a new window
    inp = nameInput.get(1.0, "end-1c")
    
    newWindow = tk.Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("collecting data")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")


    # A Label widget to show in toplevel
    tk.Label(newWindow,
        text ="Start Collecting data").pack()
    FaceCollector(inp,100)




label = tk.Label(master,
			text ="This is the main window")

label.pack(pady = 10)
nameInput = tk.Text(master,
                   height = 5,
                   width = 20)
nameInput.pack()
print(nameInput)
# a button widget which will open a
# new window on button click
btn =tk.Button(master,
			text ="Start Collecting data",
			command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
tk.mainloop()

