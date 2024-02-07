# here we want another tkinter window that has several options
# these are the preloaded animations and clicking one will run it 
# we want to make it so that for this window once the chosen animation runs 
# it will not close this tkinter window and it remains open so that they can 
# select another one to play. 

# NOTE: THIS FILE MUST BE OPENED VIA Main.py TO WORK PROPERLY 


# import the needed GUI library  
from customtkinter import *

def close_window():
    app.destroy()        # DESTROY STILL WORKS IN CUSTOM TKINTER 

# this is a class which is only used to store a class variable, 
# this class variable is altered by the user's selection made on this 
# screen and feeds the arguement to the PreloadedAnimations.py file 
# as to what preloaded animation it should compile. 

class InputHolder:
    
    UserInput = None
    

class App(CTk):
    
    def __init__(self):
        super().__init__()
        # GUI window properties
        self.geometry("800x600")  # size variable to change on pi 
        self.resizable(False, False)
        self.title("Animaster")
        
        # settings for the overall GUI theme 
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        # the frame which will contain the elements of the GUi 
        self.frame = CTkFrame(master = self)
        self.frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
        

        # label for the title of the program 
        self.label_title = CTkLabel(master = self.frame, text = "Animation Library", text_color = "black", width = 2000,
                                     height = 2, font = ("Georgia", 60), corner_radius = 8, anchor = "center", 
                                     bg_color = "white")
        self.label_title.place(relx = 0.5, rely = 0.1, anchor = "center")

        # label for the phrase associated with the program 
        self.label_phrase = CTkLabel(master = self.frame, text = "Select an Animation to Compile", text_color = "white", 
                                     width = 120, height = 1, font = ("Century Gothic", 20), corner_radius = 8, anchor = "center")
        self.label_phrase.place(relx = 0.5, rely = 0.19, anchor = "center")

        # button for launching the preloaded animation library
        self.btn = CTkButton(master = self.frame, text = "Gojo", corner_radius = 32, fg_color = "white", border_color = "blue",
                             border_width = 2, text_color = "black", height = 50, width = 50, hover_color = "light blue", font = ("Century Gothic", 20),
                             command = self.change_input_gojo)
        self.btn.place(relx = 0.2, rely = 0.5, anchor = "center")

        # button for launching the image capture software
        self.btn2 = CTkButton(master = self.frame, text = "Sukuna", corner_radius = 32, fg_color = "white", border_color = "blue",
                              border_width = 2, text_color = "black", height = 50, width = 50, hover_color = "light blue", font = ("Century Gothic", 20),
                              command = self.change_input_sukuna)
        self.btn2.place(relx = 0.8, rely = 0.5, anchor = "center")

        self.btn3 = CTkButton(master = self.frame, text = "Confirm", corner_radius = 32, fg_color = "white", border_color = "blue",
                              border_width = 2, text_color = "black", height = 50, width = 50, hover_color = "light blue", font = ("Century Gothic", 20),
                              command = close_window)
        self.btn3.place(relx = 0.8, rely = 0.9, anchor = "center")
    
       
        
    # functions that allow users to select animations 
    
    def change_input_gojo(self):
        InputHolder.UserInput = "Gojo"
        
    def change_input_sukuna(self):
        InputHolder.UserInput = "Sukuna"


app = App()
app.mainloop()

    
    
