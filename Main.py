
# RUN THIS FILE 
# Name: Chandler Dees
# Date: 2 - 8 - 23 
# Desc: The main file containing the user interface, all other elements
#       of the software are interconnected and can be accessed as soon 
#       as this program is launched.

# importing with * to avoid having to type customtkinter
# before everything
from customtkinter import *
from PIL import Image
import os

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
        self.frame_1 = CTkFrame(master=self)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        # label for the title of the program 
        self.label_title = CTkLabel(master=self.frame_1, text="Animaster", text_color="black", width=2000,
                                     height=2, font=("Century Gothic", 60), corner_radius=8, anchor="center", 
                                     bg_color="white")
        self.label_title.place(relx=0.5, rely=0.1, anchor="center")

        # label for the phrase associated with the program 
        self.label_phrase = CTkLabel(master=self.frame_1, text="You Are the Master of Your Own Creation", text_color="white", 
                                     width=120, height=1, font=("Century Gothic", 20), corner_radius=8, anchor="center")
        self.label_phrase.place(relx=0.5, rely=0.19, anchor="center")

        # button for launching the preloaded animation library
        self.btn = CTkButton(master=self.frame_1, text="Animation Library", corner_radius=32, fg_color="white", border_color="blue",
                             border_width=2, text_color="black", height=50, width=50, hover_color="light blue", font=("Century Gothic", 20),
                             command=self.openPreBuilt)
        self.btn.place(relx=0.2, rely=0.5, anchor="center")

        # button for launching the image capture software
        self.btn2 = CTkButton(master=self.frame_1, text="Image Capture", corner_radius=32, fg_color="white", border_color="blue",
                              border_width=2, text_color="black", height=50, width=50, hover_color="light blue", font=("Century Gothic", 20),
                              command=self.openImageCapture)
        self.btn2.place(relx=0.8, rely=0.5, anchor="center")

        # button for exiting the software
        self.btn3 = CTkButton(master=self.frame_1, text="Exit", corner_radius=32, fg_color="white", border_color="red",
                              border_width=2, text_color="black", height=50, width=800, hover_color="pink", font=("Century Gothic", 20),
                              command=self.quitProgram)
        self.btn3.place(relx=0.5, rely=0.9, anchor="center")
        
        # image previews for the choices 
        #preloaded_img = CTkImage(Image.open("bgtest.jpg"), size = (200, 200))
        
        #button = CTkButton(master=app,image = preloaded_img, text="",width=200,height=200,compound='left')
        #button.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        
        # Loading Image for GUI (above preloaded)
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = CTkImage(Image.open(current_path + "/ImageFolder/MickeyModelSheet.jpg"),
                                               size=(150, 125))
        self.bg_image_label = CTkLabel(self, image=self.bg_image)
        self.bg_image_label.place(relx = 0.15,rely = 0.25)
        
        # Loading Image for GUI (above Image capture)
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = CTkImage(Image.open(current_path + "/ImageFolder/MickeyModelSheet.jpg"),
                                               size=(150, 125))
        self.bg_image_label = CTkLabel(self, image=self.bg_image)
        self.bg_image_label.place(relx = 0.15,rely = 0.25)
        


    # Functions that allow this window to launch the other windows/ exit
    def openPreBuilt(self):
        os.execvp("python", ["python", "PreloadedAnimations.py"])
    
    def openImageCapture(self):
        os.execvp("python", ["python", "ImageCaptureFINAL.py"])
    
    def quitProgram(self):
        self.quit() 

app = App()
app.mainloop()
