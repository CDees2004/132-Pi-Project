# you must pip install custom tkinter
# importing with * to avoid having to type customtkinter
# before everything

from customtkinter import *
from PIL import Image, ImageTk

# initializing the Ctk Window and its size 
app = CTk()
app.geometry("800x600")         # size variable to change on pi 
app.title("Animaster")

# settings the appearance 
set_appearance_mode("dark")
set_default_color_theme("blue")

# functions used to execute the other programs from this window 
def openPreBuilt():
    os.execvp("python", ["python", "AnimRunTesting.py"])
    
def openImageCapture():
    os.execvp("python", ["python", "ImageCaptureFINAL.py"])

#############################################################################################

frame_1 = CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


# label that serves as the title for the window 
label_title = CTkLabel(master = app, text = "Animaster", text_color = "black",  width = 2000,
                       height = 2, font = ("Century Gothic", 60), corner_radius = 8, anchor = "center", 
                       bg_color = "white")

label_title.place(relx = 0.5, rely = 0.1, anchor = "center")

# label with the phrase on it 

label_phrase = CTkLabel(master = frame_1, text = "You Are the Master of Your Own Creation", text_color = "white", 
                        width = 120, height = 1, font = ("Century Gothic", 20), corner_radius = 8, anchor = "center")

label_phrase.place(relx = 0.5, rely = 0.19, anchor = "center")

# button to launch the preloaded animation library 
btn = CTkButton(master = frame_1 , text = "Animation Library", corner_radius = 32, fg_color = "white", border_color = "blue",
                border_width = 2, text_color = "black", height = 50, width = 800, hover_color= "lavender", font = ("Century Gothic", 20),
                command = openPreBuilt)

btn.place(relx = 0.5, rely = 0.3, anchor = "center")


# button to launch the image capture software
btn2 = CTkButton(master = frame_1 , text = "Image Capture", corner_radius = 32, fg_color = "white", border_color = "blue",
                border_width = 2, text_color = "black", height = 50, width = 800, hover_color= "lavender", font = ("Century Gothic", 20),
                command = openImageCapture)

btn2.place(relx = 0.5, rely = 0.4, anchor = "center")


app.mainloop()
# keeping this window open 