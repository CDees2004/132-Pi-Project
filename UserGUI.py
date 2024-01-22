# initial goal is to simply create a tkinter GUI with the ability 
# to open a PyGame GUI. This could serve as the place for the users 
# to customize their settings that will apply to the animation software

#KEY POINT: need to allow this GUI to influence the settings in the 
# animation software... somehow. 

import tkinter as tk
import subprocess

def open_file():
    subprocess.run(["python", "AnimationTest.py"])

# Create the main Tkinter window
root = tk.Tk()

# Create a button that, when clicked, calls the open_file function
button = tk.Button(root, text="Open Other Script", command=open_file)
button.pack()

# Run the Tkinter event loop
root.mainloop()

