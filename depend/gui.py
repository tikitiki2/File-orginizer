import customtkinter as tkk
import tkinter
#TODO finish later
class gui:
    def __init__(self):
        self.app = tkk.CTk()
        self.app.geometry('500x400')
        self.create_gui()




        #main loop always run last
        self.app.mainloop()


    def create_gui(self):
        self.entry = tkk.CTkEntry(master=self.app, placeholder_text="Enter Path", )
        self.entry.pack()
        self.button=tkk.CTkButton(master=self.app,command=self.path)
        self.button.pack(padx=0,pady=0)
    def path(self):
        print(self.entry.get())



#https://github.com/TomSchimansky/CustomTkinter/wiki/CTkOptionMenu
gui()