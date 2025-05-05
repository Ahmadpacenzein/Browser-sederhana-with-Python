
import customtkinter as ctk
from tkinter import messagebox
from main_program import main_browser
import re

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class BrowserApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter Web Browser")
        self.geometry("800x600")

        self.url_entry = ctk.CTkEntry(self, width=600, placeholder_text="Masukkan URL di sini...")
        self.url_entry.pack(pady=(20, 10))
        self.url_entry.insert(0, "http://data.pr4e.org/romeo.txt")

        self.fetch_button = ctk.CTkButton(self, text="Ambil Halaman", command=self.fetch_and_display)
        self.fetch_button.pack(pady=10)

        self.output_text = ctk.CTkTextbox(self, width=750, height=450, wrap="word")
        self.output_text.pack(padx=10, pady=10)

    def fetch_and_display(self):
        url = self.url_entry.get()
        content, error = main_browser(url)
        self.output_text.delete("0.0", "end")

        if error:
            messagebox.showerror("Error", error)
            return

        self.output_text.insert("0.0", content)

        tag_pattern = re.compile(r"</?[a-zA-Z][^>]*>")
        for match in tag_pattern.finditer(content):
            start_index = f"0.0+{match.start()}c"
            end_index = f"0.0+{match.end()}c"
            self.output_text.tag_add("tag", start_index, end_index)

        self.output_text.tag_config("tag", foreground="#0099ff")


if __name__ == "__main__":
    app = BrowserApp()
    app.mainloop()
