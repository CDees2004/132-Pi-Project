# here we want another tkinter window that has several options
# these are the preloaded animations and clicking one will run it 
# we want to make it so that for this window once the chosen animation runs 
# it will not close this tkinter window and it remains open so that they can 
# select another one to play. 

# import the needed libraries 
from tkinter import *

class InputHolder:
    
    UserInput = None
    

# Create the main Tkinter window


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="blue")  # Set background color

        self.button1 = Button(master, text="Gojo Anim.", fg="black", bg="lightblue", bd=2, height=3, font=("Helvetica", 14, "bold"), command = self.change_input_gojo)
        self.button1.pack(side=TOP, fill=X, pady=5)

        self.button2 = Button(master, text="Sukuna Anim.", fg="white", bg="red", height=3, font=("Helvetica", 14, "bold"), command = self.change_input_sukuna)
        self.button2.pack(side=TOP, fill=BOTH, pady=5)

        #self.button3 = Button(master, text="------ Anim.", fg="white", bg="darkred", height=3, font=("Helvetica", 14, "bold"), command = openSettings)
        #self.button3.pack(side=TOP, fill=BOTH, pady=5)

        #self.button4 = Button(master, text="------ Anim.", fg="white", bg="green", height=3, font=("Helvetica", 14, "bold"), command = self.quit)
        #self.button4.pack(side=TOP, fill=BOTH, pady=5)
        
    def change_input_gojo(self):
        InputHolder.UserInput = "Gojo"
        
    def change_input_sukuna(self):
        InputHolder.UserInput = "Sukuna"

        

window = Tk()
window.title("User Interface")  # Set window title
app = App(window)
window.geometry("800x800")
window.configure(bg="black")  # Set window background color
window.mainloop()
