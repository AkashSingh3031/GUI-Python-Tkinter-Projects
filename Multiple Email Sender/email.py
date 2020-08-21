from tkinter import *
from PIL import Image, ImageTk

class Bulk_Email:
    def __init__(self, root):
        self.root = root
        self.root.title("BULK EMAIL APPLICATION")
        self.root.geometry("1000x550+200+50")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        #================ ICON ==================
        self.email_icon = ImageTk.PhotoImage(file = "images/email2.png")
        self.setting_icon = ImageTk.PhotoImage(file = "images/setting.png")

        #================ TITLE =================
        title = Label(self.root, text="Bulk Email Send Panel", image=self.email_icon, compound=LEFT, font=("Groudy old Style", 48, "bold"), bg="#222A35", fg="white", anchor="w").place(x=0, y=0, relwidth=1)



root = Tk()
obj = Bulk_Email(root)
root.mainloop()