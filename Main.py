# you must pip install custom tkinter
# importing with * to avoid having to type customtkinter
# before everything

from customtkinter import *
from PIL import Image, ImageTk

# settings the appearance 
set_appearance_mode("dark")
set_default_color_theme("blue")


# functions used to execute the other programs from this window 
def openPreBuilt():
    os.execvp("python", ["python", "AnimRunTesting.py"])


# initializing the Ctk Window and its size 
app = CTk()
app.geometry("800x600")         # size variable to change on pi 

label_title = CTkLabel(master = app, text = "Main Title", width = 120, height = 25, corner_radius = 8)
label_title.place(relx = 0.5, rely = 0.1, anchor = "center")

btn = CTkButton(master = app , text = "Click me", corner_radius = 32, fg_color = "white", border_color = "blue",
                border_width = 2, text_color = "black", command = openPreBuilt)

my_image = CTkImage(Image.open("bgtest.JPG"), size = (26, 26))

button_image = CTkButton(app, image = my_image)

#btn.pack()
btn.place(relx = 0.5, rely = 0.2, anchor = "center")

ent = CTkEntry(master = app)
ent.place(relx = 0.5, rely = 0.3, anchor = "center")

app.mainloop()
# keeping this window open 