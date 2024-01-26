
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
        Frame.__init__(self, master, bg="blue")  # Set background color

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
window.configure(bg="black")  # Set window background color
window.mainloop()