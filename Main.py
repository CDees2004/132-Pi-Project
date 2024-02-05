# you must pip install custom tkinter
# importing with * to avoid having to type customtkinter
# before everything
from customtkinter import *
import os

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")  # size variable to change on pi 
        self.title("Animaster")
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        self.frame_1 = CTkFrame(master=self)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_title = CTkLabel(master=self, text="Animaster", text_color="black", width=2000,
                                     height=2, font=("Century Gothic", 60), corner_radius=8, anchor="center", 
                                     bg_color="white")
        self.label_title.place(relx=0.5, rely=0.1, anchor="center")

        self.label_phrase = CTkLabel(master=self.frame_1, text="You Are the Master of Your Own Creation", text_color="white", 
                                     width=120, height=1, font=("Century Gothic", 20), corner_radius=8, anchor="center")
        self.label_phrase.place(relx=0.5, rely=0.19, anchor="center")

        self.btn = CTkButton(master=self.frame_1, text="Animation Library", corner_radius=32, fg_color="white", border_color="blue",
                             border_width=2, text_color="black", height=50, width=50, hover_color="lavender", font=("Century Gothic", 20),
                             command=self.openPreBuilt)
        self.btn.place(relx=0.2, rely=0.5, anchor="center")

        self.btn2 = CTkButton(master=self.frame_1, text="Image Capture", corner_radius=32, fg_color="white", border_color="blue",
                              border_width=2, text_color="black", height=50, width=50, hover_color="lavender", font=("Century Gothic", 20),
                              command=self.openImageCapture)
        self.btn2.place(relx=0.8, rely=0.5, anchor="center")

        self.btn3 = CTkButton(master=self.frame_1, text="Exit", corner_radius=32, fg_color="white", border_color="red",
                              border_width=2, text_color="black", height=50, width=800, hover_color="pink", font=("Century Gothic", 20),
                              command=self.quitProgram)
        self.btn3.place(relx=0.5, rely=0.9, anchor="center")

    def openPreBuilt(self):
        os.execvp("python", ["python", "PreloadedAnimations.py"])
    
    def openImageCapture(self):
        os.execvp("python", ["python", "ImageCaptureFINAL.py"])
    
    def quitProgram(self):
        self.quit() 

app = App()
app.mainloop()
