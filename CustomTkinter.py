# you must pip install custom tkinter

from customtkinter import * 

app = CTk()
app.geometry("800x600")
set_appearance_mode("dark")

label_title = CTkLabel(master = app, text = "User Interface Title", width = 120, height = 25, corner_radius = 8)
label_title.place(relx = 0.5, rely = 0.1, anchor = "center")

btn = CTkButton(master = app , text = "Click me", corner_radius = 32, fg_color = "white", border_color = "blue",
                border_width = 2, text_color = "black")

#btn.pack()
btn.place(relx = 0.5, rely = 0.2, anchor = "center")

ent = CTkEntry(master = app)
ent.place(relx = 0.5, rely = 0.3, anchor = "center")

app.mainloop()
