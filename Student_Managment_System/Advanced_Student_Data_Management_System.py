from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('1500x850+0+0')
root.title("Advanced Student Data Base Management System")
root.iconbitmap("student.ico")
root.config(bg="pink")

stLabel = Label(root, text="Advanced Student Data Base Management System", background="yellow", foreground="red",
           font='times 30   bold', relief=RIDGE, bd=5, anchor='center')
stLabel.pack(side=TOP, fill=X)

#------------------------------------ FRAME-1 --------------------------------------------------------
btnFrame = Frame(root, bg="crimson", relief=RIDGE, borderwidth=4,)
btnFrame.place(x=0, y=55, width=150, height=740)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@  BUTTONS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
image1 = Image.open("home.jpg")
image1 = image1.resize((140, 140), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(image1)
#++++++++++++++
home = Button(btnFrame, image=img1, text="HOME", width=140, height=140, font='times 10   bold')
home.grid(row=0, column=0, pady=0)

image2 = Image.open("st.jpg")
image2 = image2.resize((140, 140), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(image2)
#++++++++++++++
st = Button(btnFrame, image=img2, text="Manage\n Student", width=140, height=140, font='times 10   bold')
st.grid(row=1, column=0, pady=0)

image3 = Image.open("viewSt.png")
image3 = image3.resize((140, 140), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(image3)
#++++++++++++++
viewSt = Button(btnFrame, image=img3, text="View\n Student", width=140, height=140, font='times 10   bold')
viewSt.grid(row=2, column=0, pady=0)

image4 = Image.open("viewAll.png")
image4 = image4.resize((140, 140), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(image4)
#++++++++++++++
viewAll = Button(btnFrame, image=img4, text="View\n All", width=140, height=140, font='times 10   bold')
viewAll.grid(row=3, column=0, pady=0)

image5 = Image.open("exit.png")
image5 = image5.resize((140, 140), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(image5)
#++++++++++++++
exit = Button(btnFrame, image=img5, text="Exit", width=140, height=140, font='times 10   bold')
exit.grid(row=4, column=0, pady=0)



#------------------------------------ LABEL__FRAME-2--------------------------------------------------------------------

#!!!!!!!!!!!!!!!!!!!!!!!! Home_Frame !!!!!!!!!!!!!!!!!!!!!!!!!!!
homeFrame = LabelFrame(root, text="Dashboard/Home", bg='cyan', relief=RIDGE, borderwidth=0, foreground="green",
                       font="times 20 bold")
homeFrame.place(x=150, y=55, width=1380, height=740)
#+++++++++++++++++++++++++++++++++++++++++++
image = Image.open("profile.jpg")
image = image.resize((1370, 740), Image.ANTIALIAS)
img_bg = ImageTk.PhotoImage(image)
imgLabel = Label(homeFrame, image=img_bg)
imgLabel.pack(fill="both", expand="yes")
#==========================================
l1 = Label(homeFrame, text='Total Students', borderwidth=4, bg='red', bd=6, relief=GROOVE,
           font='roman 30 italic bold', fg='yellow')
l1.place(x=100, y=100, width=600, height=60)
f1 = Frame(homeFrame, ).pack() 

l2 = Label(homeFrame, text='About Developer', borderwidth=4, bg='green', bd=6, relief=GROOVE,
           font='roman 30 italic bold', fg='pink3')
l2.place(x=750, y=100, width=600, height=60)


#!!!!!!!!!!!!!!!!!!!!!!!! Student_Frame !!!!!!!!!!!!!!!!!!!!!!!!!!!
stFrame = LabelFrame(root, text="Dashboard/Student", bg='cyan', relief=RIDGE, borderwidth=0, foreground="green",
                       font="times 20 bold")
stFrame.place(x=150, y=55, width=1380, height=740)
#+++++++++++++++++++++++++++++++++++++++++++
image = Image.open("profile.jpg")
image = image.resize((1370, 740), Image.ANTIALIAS)
img_bg = ImageTk.PhotoImage(image)
imgLabel = Label(stFrame, image=img_bg)
imgLabel.pack(fill="both", expand="yes")
#==========================================




root.mainloop()