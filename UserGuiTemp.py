
# import the needed libraries 
from tkinter import *
import os 

# function that launches animation software when called

def openPreBuilt():
    os.execvp("python", ["python", "AnimationFoldTest.py"])

def openImageCapture():
    os.execvp("python", ["python", "CameraTesting.py"])
    
def openSettings():
    os.execvp("python", ["python", "UserSettings.py"])

# Create the main Tkinter window


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")  # Set background color

        self.button1 = Button(master, text="Image Capture Animation", fg="black", bg="lightblue", bd=2, height=3, font=("Helvetica", 14, "bold"), command = openImageCapture)
        self.button1.pack(side=TOP, fill=X, pady=5)

        self.button2 = Button(master, text="View Prebuilt Animations", fg="white", bg="red", height=3, font=("Helvetica", 14, "bold"), command = openPreBuilt)
        self.button2.pack(side=TOP, fill=BOTH, pady=5)

        self.button3 = Button(master, text="Settings", fg="white", bg="darkred", height=3, font=("Helvetica", 14, "bold"), command = openSettings)
        self.button3.pack(side=TOP, fill=BOTH, pady=5)

        self.button4 = Button(master, text="Exit", fg="white", bg="green", height=3, font=("Helvetica", 14, "bold"), command = self.quit)
        self.button4.pack(side=TOP, fill=BOTH, pady=5)


window = Tk()
window.title("User Interface")  # Set window title
app = App(window)
window.geometry("800x800")
window.configure(bg="white")  # Set window background color
window.mainloop()
































'''
from tkinter import *

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")  # Set background color

        self.button1 = Button(master, text="ANIMATE", fg="black", bg="lightblue", bd=2, height=3, font=("Helvetica", 14, "bold"))
        self.button1.pack(side=TOP, fill=X, pady=5)

        self.button2 = Button(master, text="PAUSE", fg="white", bg="red", command=self.say, height=3, font=("Helvetica", 14, "bold"))
        self.button2.pack(side=TOP, fill=BOTH, pady=5)

        self.button3 = Button(master, text="STOP", fg="white", bg="darkred", height=3, font=("Helvetica", 14, "bold"))
        self.button3.pack(side=TOP, fill=BOTH, pady=5)

        self.button4 = Button(master, text="PLAY", fg="white", bg="green", height=3, font=("Helvetica", 14, "bold"))
        self.button4.pack(side=TOP, fill=BOTH, pady=5)

    def say(self):
        print("Pausing Process...")

window = Tk()
window.title("Awesome GUI")  # Set window title
app = App(window)
window.geometry("550x430")
window.configure(bg="white")  # Set window background color
window.mainloop()
'''





























'''
from tkinter import * # The star means essentially everything

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(master, text="ANIMATE", fg="black", bg="white", bd="2", height=8)
        self.button1.pack(side=TOP, fill=X)
        self.button2 = Button(master, text="PAUSE", fg="red", bg ="gray64", command=self.say, height=8)
        self.button2.pack(side=TOP, fill=BOTH)
        self.button3 = Button(master, text="STOP", fg="white", bg="red", height=8)
        self.button3.pack(side=TOP, fill=BOTH)
        self.button4 = Button(master, text="PLAY", fg="orange", height=8)
        self.button4.pack(side=TOP, fill=BOTH)

    def say(self):
        print("Pausing Process...")

window = Tk()
app = App(window)
window.geometry("550x430")
window.mainloop()

'''
'''
from tkinter import *

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Configure grid options
        self.grid(row=0, column=0, padx=10, pady=10)

        # Create buttons
        self.button1 = Button(master, text="ANIMATE", fg="black", bg="white", bd=2, width=15)
        self.button1.grid(row=0, column=0, columnspan=2, 
        self.button2 = Button(master, text="PAUSE", fg="red", bg="gray64", command=self.say, width=15)
        self.button2.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        self.button3 = Button(master, text="STOP", fg="white", bg="red", width=15)
        self.button3.grid(row=2, column=0, pady=(0, 10))

        self.button4 = Button(master, text="PLAY", fg="orange", width=15)
        self.button4.grid(row=2, column=1, pady=(0, 10))

    def say(self):
        print("Pausing Process...")

window = Tk()
app = App(window)
window.geometry("300x200")
window.title("Symmetrical Tkinter App")
window.mainloop()
'''