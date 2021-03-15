def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.Resume_Button.grid_remove()
    root.Pause_Button.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='playing...')

def volumeup():
    vol = mixer.music.get_volume()
    if vol >= vol*100:
        mixer.music.set_volume(vol+0.1)
    else:
        mixer.music.set_volume(vol+0.05)
    progressbar_volume_Label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value'] = mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    if vol <= vol*100:
        mixer.music.set_volume(vol-0.05)
    else:
        mixer.music.set_volume(vol-0.05)
    progressbar_volume_Label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value'] = mixer.music.get_volume()*100

def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text="Stop")

def pausemusic():
    mixer.music.pause()
    root.Pause_Button.grid_remove()
    root.Resume_Button.grid()
    AudioStatusLabel.configure(text="Paused")

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    Progressbar_lbl.grid()
    root.mutebutton.grid()
    mixer.music.play()
    progressbar_music_Label.grid()
    mixer.music.set_volume(0.4)
    progressbar_volume['value'] = 40
    progressbar_volume_Label['text'] = '40%'
    AudioStatusLabel.configure(text="Playing...")

    song = MP3(ad)
    total_song_Length = int(song.info.length)
    progressbar_music['maximum'] = total_song_Length
    progressbar_music_StartEnd.configure(text='{}'.format(str(datetime.timedelta(seconds=total_song_Length))))

    def func():
        current_song_Length = mixer.music.get_pos()//1000
        progressbar_music['value'] = current_song_Length
        progressbar_music_StartEnd.configure(text='{}'.format(str(datetime.timedelta(seconds=current_song_Length))))
        progressbar_music.after(2,func)
    func()

def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='C:\\Users\\Akash Singh\\Documents\\Coding\\Python Program\\Projects\\GUI Project\\Music Player\\Music_Player\\songs',
                                        title='Select Audio File',
                                        filetype=(('MP3', '*.mp3'), ('WAV', '*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File',
                                        filetype=(('MP3', '*.mp3'), ('WAV', '*.wav')))
    audiotrack.set(dd)

def createwidthes():
    global imbrowse, implay, impause, imstop, imvolumeup, imvolumedown, immute, imresume, imunmute
    global progressbar_music_StartEnd, progressbar_music_StartTime, progressbar_music
    global AudioStatusLabel, Progressbar_lbl, progressbar_volume, progressbar_volume_Label, progressbar_music_Label

    #==============================Image Path==================================
    # immute = PhotoImage(file = '')
    # imunmute = PhotoImage(file = '')
    # implay = PhotoImage(file = '')
    # imstop = PhotoImage(file = '')
    # impause = PhotoImage(file = '')
    # imresume = PhotoImage(file = '')
    # imbrowse = PhotoImage(file = '')
    # imvolumeup = PhotoImage(file = '')
    # imvolumedown = PhotoImage(file = '')

    # #==============================Image Path==================================
    immute = PhotoImage(file = 'images/mute.png')
    imunmute = PhotoImage(file = 'images/volume_down.png')
    implay = PhotoImage(file = 'images\\play.png')
    imstop = PhotoImage(file = 'images\\stop.png')
    impause = PhotoImage(file = 'images\\pause.png')
    imresume = PhotoImage(file = 'images\\resume.png')
    imbrowse = PhotoImage(file = 'images\\search.png')
    imvolumeup = PhotoImage(file = 'images\\volume_up.png')
    imvolumedown = PhotoImage(file = 'images\\volume_down.png')

    #==============================Chenge Image Size==================================
    imbrowse = imbrowse.subsample(22,22)
    implay = implay.subsample(8,8)
    impause = impause.subsample(17,17)
    imresume = imresume.subsample(17,17)
    imstop = imstop.subsample(10,10)
    imvolumeup = imvolumeup.subsample(8,8)
    imvolumedown = imvolumedown.subsample(8,8)
    immute = immute.subsample(8,8)
    imunmute = imunmute.subsample(8,8)

    #==============================Label==================================
    # music_Label = Label(root, text="Music Player", font=('arial', 30, 'bold'), bg="#1f1f2e", fg="white")
    # music_Label.grid(row=0, column=1, pady=5)
    
    # TrackLabel = Label(root, text="Select Audio Track: ", font=('arial', 18, 'bold'), bg="#262626", fg="white")
    # TrackLabel.grid(row=1, column=0, padx=20, pady=20)

    AudioStatusLabel = Label(root, text="", font=('arial', 18, 'bold'), bg="#8533ff", fg="white")
    AudioStatusLabel.grid(row=3, column=1)

    #==============================Entry box==================================
    Track_Label_Entry = Label(root, font=('arial', 20, 'bold'), bg="#9999ff", width=32, textvariable=audiotrack)
    Track_Label_Entry.grid(row=1, column=1, padx=20, pady=20)

    #==============================Button==================================
    Browse_Button = Button(root, text="Search", font=('arial', 13, 'bold'), bg="#333333", fg="white", width=150, height=27, bd=5, activebackground="#333333", image=imbrowse, compound=RIGHT, command=musicurl)
    Browse_Button.grid(row=1, column=0, padx=0, pady=0)

    Play_Button = Button(root, text="Play", font=('arial', 13, 'bold'), bg="#7300e6", fg="white", width=150, height=27, bd=5, activebackground="purple4", image=implay, compound=RIGHT, command=playmusic)
    Play_Button.grid(row=2, column=0, padx=20, pady=20)

    root.Pause_Button = Button(root, text="Pause", font=('arial', 13, 'bold'), bg="#6600cc", fg="white", width=150, height=27, bd=5, activebackground="purple4", image=impause, compound=RIGHT, command=pausemusic)
    root.Pause_Button.grid(row=4, column=0, padx=20, pady=20)

    root.Resume_Button = Button(root, text="Resume", font=('arial', 13, 'bold'), bg="#7300e6", fg="white", width=150, height=27, bd=5, activebackground="purple4", image=imresume, compound=RIGHT, command=resumemusic)
    root.Resume_Button.grid(row=4, column=0, padx=20, pady=20)
    root.Resume_Button.grid_remove()

    root.mutebutton = Button(root, text="Mute", font=('arial', 15, 'bold'), bg="#9999ff", fg="white", width=100, height=27, bd=5, activebackground="purple4", image=immute, compound=RIGHT, command=mutemusic)
    root.mutebutton.grid(row=6, column=3)
    root.mutebutton.grid_remove()

    root.unmutebutton = Button(root, text="Unmute", font=('arial', 15, 'bold'), bg="#9999ff", width=100, bd=5, activebackground="purple4", image=imunmute, compound=RIGHT, command=unmutemusic)
    root.unmutebutton.grid(row=6, column=3)
    root.unmutebutton.grid_remove()

    Volume_Up_Button = Button(root, text="Volume UP", font=('arial', 13, 'bold'), bg="#7300e6", fg="white", width=150, bd=5, activebackground="purple4", image=imvolumeup, compound=RIGHT, command=volumeup)
    Volume_Up_Button.grid(row=0, column=2, padx=20, pady=20)

    Stop_Button = Button(root, text="Stop", font=('arial', 13, 'bold'), bg="#7300e6", fg="white", width=150, height=27, bd=5, activebackground="purple4", image=imstop, compound=RIGHT, command=stopmusic)
    Stop_Button.grid(row=3, column=0, padx=20, pady=20)

    Volume_Down_Button = Button(root, text="Volume Down", font=('arial', 13, 'bold'), bg="#7300e6", fg="white", width=150, height=27, bd=5, activebackground="purple4", image=imvolumedown, compound=RIGHT, command=volumedown)
    Volume_Down_Button.grid(row=0, column=0, padx=20, pady=20)

    #==============================Progressbar Valume UP Down==================================
    Progressbar_lbl = Label(root, text="", bg="red")
    Progressbar_lbl.grid(row=0, column=1, rowspan=1)
    Progressbar_lbl.grid_remove()

    progressbar_volume = Progressbar(Progressbar_lbl, orient=HORIZONTAL, mode="determinate", value=40, length=190)
    progressbar_volume.grid(row=0, column=0, ipadx=5)

    progressbar_volume_Label = Label(Progressbar_lbl, text="40%",bg="lightgray", width=3)
    progressbar_volume_Label.grid(row=0, column=0)

    #==============================Progressbar Running Time==================================
    progressbar_music_Label = Label(root, text="", bg="#9999ff")
    progressbar_music_Label.grid(row=10, column=0, columnspan=3, padx=20, pady=20)
    progressbar_music_Label.grid_remove()

    progressbar_music_StartTime = Label(progressbar_music_Label, text="0:00:00", bg="#9999ff", width=7)
    progressbar_music_StartTime.grid(row=0, column=0)

    progressbar_music = Progressbar(progressbar_music_Label, orient=HORIZONTAL, mode="determinate", value=0)
    progressbar_music.grid(row=0, column=1, ipadx=380, ipady=0)

    progressbar_music_StartEnd = Label(progressbar_music_Label, text="0:00:00", bg="#9999ff")
    progressbar_music_StartEnd.grid(row=0, column=2)



    #============================================================================================

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
import random

root = Tk()
root.geometry("1200x600+200+50")
root.title("Music Player")
root.iconbitmap("C:\\Users\\Akash Singh\\Documents\\Coding\\Python Program\\Projects\\GUI Project\\Music Player\\Music_Player\\images\\media_player.ico")
root.resizable(False, False)
root.configure(background="brown")

#===================================Global Variable

audiotrack = StringVar()
currentvol = 0
total_song_Length = 0
count = 0
text = ""

#==================================Background Image
# image = Image.open("C:\\Users\\Akash Singh\\Documents\\Coding\\Python Program\\Projects\\GUI Project\\Music Player\\Music_Player\\images\\mahadev.jpg")
# image = Image.open("")
# photo = ImageTk.PhotoImage(image)

label = Label(root, background="white")
label.place(x=0, y=0)

#=================================Slider
ss = "Developer:- AKASH SINGH"

Slider_Label = Label(root, text=ss, bg="#a64dff", fg="black", font=("arial", 20, "italic bold"))
Slider_Label.grid(row=5, column=0, padx=0, pady=0, columnspan=3)



colors = ['red','pink','green','yellow','crimson','red2','gold2']
def IntoLabelColorTick():
    fg = random.choice(colors)
    Slider_Label.config(fg = fg)
    Slider_Label.after(2, IntoLabelColorTick)
  
def IntroLabelTrick():
    global count, text
    if count>=len(ss):
        count = -1
        text=""
        Slider_Label.configure(text=text)
    else:
        text = text+ss[count]
        Slider_Label.configure(text=text)
    count += 1
    Slider_Label.after(200, IntroLabelTrick)


IntroLabelTrick()
IntoLabelColorTick()
mixer.init()
createwidthes()
root.mainloop()