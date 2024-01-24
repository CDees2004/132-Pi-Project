# initial goal is to simply create a tkinter GUI with the ability 
# to open a PyGame GUI. This could serve as the place for the users 
# to customize their settings that will apply to the animation software

#KEY POINT: need to allow this GUI to influence the settings in the 
# animation software... somehow. 
import os 
from tkinter import *  

window = Tk()

def openFile():
    os.execvp("python", ["python", "AnimationFoldTest.py"])
# Create the main Tkinter window


button = Button(window, text = "testing", command = openFile)
button.pack()
# Create a button that, when clicked, calls the open_file function
#button = tk.Button(root, text="Open Other Script", command=openFile())
#button.pack()

# Run the Tkinter event loop
window.mainloop()

