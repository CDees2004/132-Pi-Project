from tkinter import *
from AnimRunTesting import settings

def update_variable(self):
        # create a variable that represents the users input value 
        value = self.entry1.get()
        # set that value to equal the fps
        settings.vari_fps = value 
         

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="blue")  # Set background color
        self.label1 = Label(master, text = "fps setting", fg = "black", bg = "lightblue", font = ("Helvetica", 14, "bold"))
        self.label1.pack(side = TOP , fill = X, pady = 5)
        
        self.entry1 = Entry(master, text="Input setting", fg="black", bg="lightblue", font=("Helvetica", 14, "bold"))
        self.entry1.pack(side=TOP, fill=BOTH, pady=5)


        self.button2 = Button(master, text="Enter", fg="white", bg="red", height=3, font=("Helvetica", 14, "bold"), command = update_variable)
        self.button2.pack(side=TOP, fill=BOTH, pady=5)

        self.button4 = Button(master, text="Exit", fg="white", bg="green", height=3, font=("Helvetica", 14, "bold"))
        self.button4.pack(side=TOP, fill=BOTH, pady=5)

    
        

window = Tk()
window.title("User Interface")  # Set window title
app = App(window)
window.geometry("800x800")
window.configure(bg="black")  # Set window background color
window.mainloop()


