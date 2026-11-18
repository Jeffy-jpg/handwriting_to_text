import customtkinter as ctk
import tkinter as tk
from tkinter import *

class App (ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Text Converter")
        self.geometry("1000x800")
        self.resizable(True, True)
        self._set_appearance_mode("dark")

        #grid configuration 
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight =1)
        self.grid_rowconfigure(1, weight =1)

        #top row for the grid
        self.top_right = ctk.CTkFrame(self)
        self.top_right.grid(row = 0, column = 0, padx=10,
                             pady=10, sticky ="nsew")

        self.top_left = ctk.CTkFrame(self)
        self.top_left.grid(row=0, column=1, padx=10,
                           pady=10, sticky="nsew")

        self.bottom_row = ctk.CTkFrame(self)
        self.bottom_row.grid(row=1, column=0, columnspan=2, padx=10,
                             pady=10, sticky="nsew")

        

app = App()
app.mainloop()       