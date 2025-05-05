import customtkinter as ctk

app = ctk.CTk()
app.title("Test Tampilan GUI")
app.geometry("300x200")
label = ctk.CTkLabel(app, text="Hello, CustomTkinter!")
label.pack(pady=20)
app.mainloop()