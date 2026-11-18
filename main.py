import customtkinter as ctk
import tkinter as tk
from tkinter import *

class App (ctk.CTk):

#---FUNCTIONS FOR THE BUTTONS AT THE BOTTOM OF THE TOP FRAME  
    def SetDefault(self):
        default_fg=ctk.ThemeManager.theme["CTkButton"]["fg_color"]
        default_hover=ctk.ThemeManager.theme["CTkButton"]["hover_color"]
        self.left_btn.configure(text='Capture [◉"]', command=self.ButtonSwap,
                                    fg_color=default_fg, hover_color=default_hover)
        self.right_btn.configure(text="Upload 🢁", command=self.Upload,
                                    fg_color=default_fg, hover_color=default_hover)
        print("Action cancelled/Confirmed, buttons returned to normal")
    
    def ButtonSwap(self):
        self.Capture()
        self.left_btn.configure(text="Cancel ⓧ", command=self.SetDefault, fg_color = "#E63946",
                                hover_color="#B51724")
        self.right_btn.configure(text="Confirm ✔", command = self.ConfirmAction, fg_color = "#28A745",
                                 hover_color="#218838")
            
    def ConfirmAction(self):
        self.SetDefault()
        print("Picture Successfully Uploaded") 

    def Capture(self):
        print("picture taken. Showing confirm button")

    def Upload(self):
        print("Opening upload picture menu")

    def CopyText(self):
        print("text successfully copied")

    #---MAIN APP---       
    def __init__(self):
        super().__init__()

        self.title("Text Converter")
        self.geometry("1000x800")
        self.resizable(True, True)
        self._set_appearance_mode("dark")

        #----WINDOW CONFIGURATION----
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight =2)
        self.grid_rowconfigure(1, weight =1)

        self.top = ctk.CTkFrame(self)
        self.top.grid(row=0, column=0, padx=10,
                           pady=10, sticky="nsew")

        self.bottom_row = ctk.CTkFrame(self)
        self.bottom_row.grid(row=1, column=0, padx=10,
                             pady=10, sticky="nsew")


        #---TOP PANEL GRID CONFIGURATION---
        self.top.grid_rowconfigure(0, weight=9)
        self.top.grid_rowconfigure(1, weight=1)
        self.top.grid_columnconfigure(0, weight=1)


        #---Camera Frame---
        #TODO CHANGE COLOUR
        self.cam_display_frame = ctk.CTkFrame(self.top, corner_radius= 0,
                                               fg_color= "red")
        self.cam_display_frame.grid(row=0, column=0, sticky="nsew")

        #TODO this is to be removed when camera feed in added
        temp_btn_00 = ctk.CTkLabel(self.cam_display_frame,
                                      text="Camera feed would go here",
                                      font= ("arial", 25, "bold"))
        temp_btn_00.pack()

        #---Button Frame
        self.cam_btn_frame = ctk.CTkFrame(self.top, corner_radius= 0,
                                          fg_color="transparent")
        self.cam_btn_frame.grid(row=1, column=0, sticky="nsew")

        #centers buttons at the bottom
        center_wrapper00 = ctk.CTkFrame(self.cam_btn_frame, corner_radius=0)
        center_wrapper00.pack(expand=True)

        #button to capture and swapped to button to cancel
        self.left_btn = ctk.CTkButton(center_wrapper00, text = 'Capture [◉"]',
                                             font=("arial", 20, "bold"), corner_radius=8,
                                             command=self.ButtonSwap)
        self.left_btn.pack(side=LEFT, ipadx = 20, ipady = 20, padx=(0, 10))

        #button to upload and then swapped to confirm
        self.right_btn = ctk.CTkButton(center_wrapper00, text="Upload 🢁", font=("arial", 20, "bold"),
                                              corner_radius=8)
        self.right_btn.pack(side=RIGHT, ipadx = 20, ipady = 20, padx=(10, 0)) 

        #---BOTTOM PANEL CONFIGURATION


        #using an imput frame so the text can be edited
        #TODO CHANGE COLOUR
        self.input_frame= ctk.CTkFrame(self.bottom_row, corner_radius= 0, fg_color="blue")
        self.input_frame.pack(side = TOP, fill= BOTH, expand=True)

        self.text_entry = ctk.CTkTextbox(self.input_frame,
                                       font=("arial", 12))
        self.text_entry.pack(fill = BOTH, expand = True)
        self.text_entry.insert("0.0", "Scanned will be displayed here...")


        #copy button at the bottom of the frame
        #TODO CHANGE COLOUR
        self.btn_frame= ctk.CTkFrame(self.bottom_row, corner_radius=0, fg_color="orange")
        self.btn_frame.pack(side=BOTTOM, fill= BOTH, expand=False)


        self.copy_btn=ctk.CTkButton(self.btn_frame, text = "Copy Text", font=("arial", 20, "bold"),
                                    command = self.CopyText)
        self.copy_btn.pack(pady=10, ipadx = 10, ipady = 10)
        
app = App()
app.mainloop()       