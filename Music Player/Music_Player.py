#import the libraries
from tkinter import *
from tkinter import *
from tkinter import filedialog
import pygame
import threading
from time import sleep
from selenium import common
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#opens and Plays songs offline
def openfile():
    global file
    filepath = filedialog.askopenfilename()
    file = filepath
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
#streams online songs through youtube
class YoutubeMusic():
    def __init__(self):
        self.IncreaseTime = 30
        self.DecreaseTime = 30
        self.user_agent = '--user-agent=Mozilla/5.0 (iPhone CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
        self.options = Options()
        self.CompletelyLoaded = True
        self.options.add_argument(self.user_agent)
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--log-level=3')
        self.Browser = Chrome(r'C:\Users\HP\Desktop\music player\chromedriver.exe',options=self.options)
        #our browser is read to shoot.

    #navigates to youtube
    def NavigateYoutube(self,MusicName):
        #!t Will Navigate On Youtube Website.
        self.MusicName = MusicName
        self.CompletelyLoaded = False
        print("[Loading %s On Youtube . . . ]"%self.MusicName)
        self.Browser.get("https://m.youtube.com/results?search_query=%s"%self.MusicName)
        self.Browser.implicitly_wait(5)
    #takes the list of search results and stores in the list named self.Vedios    
    def ListVideos(self):
        self.Counter = 1
        self.Videos = []
        for eachVid in range(1,4):
            self.xpath = "/html/body/ytm-app/div[3]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[%d]/div/div/a/h4/span"%eachVid
            self.EachVideo = WebDriverWait(self.Browser,10).until(EC.presence_of_element_located((By.XPATH,self.xpath)))
            self.EachVideo=self.EachVideo.text
            #self.EachVideo = self.Browser.find_element_by_xpath('/html/body/ytm-app/div[3]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[%d]/div/div/a/h4/span'%eachVid).text
            self.Videos.append(self.EachVideo)
        i = 1
        for eachVid in self.Videos:
            results.insert(END, i )
            results.insert(END, eachVid + '\n')
            i = i+1    
    #refreshes the page 
    def RefreshPage(self):
        #!In Case Of Error Refresh Can Be Done.
        self.CurrentPage = self.Browser.current_url
        self.Browser.get(self.CurrentPage)
        print("Page Refreshed.")
    #plays the song online
    def PlayVideo(self,VideoID):
        #Finally Plays Video.
        #!VIDEO PLAY CODE HERE
        self.VideoPlay = '//*[@id="app"]/div[3]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[%d]/div/div/a/h4/span'%VideoID;
        self.Video = WebDriverWait(self.Browser,10).until(EC.presence_of_element_located((By.XPATH,self.VideoPlay)))
        sleep(2)
        self.Video.click()

        self.VideoTitle = WebDriverWait(self.Browser,5).until(EC.presence_of_element_located((By.CLASS_NAME,'slim-video-metadata-title')))
        #self.VideoTitle = self.Browser.find_element_by_class_name('slim-video-metadata-title') #!To Fetch Video Title.
        self.VideoTitle = self.VideoTitle.text 
        print('[Playing %s Youtube Now... ]'%self.VideoTitle)
        self.CompletelyLoaded = True
        self.RefreshPage()
        self.GetUrl = self.Browser.find_element_by_css_selector('video.video-stream.html5-main-video')
        #self.GetUrl = WebDriverWait(self.Browser,30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'video.video-stream.html5-main-video')))
        self.GetUrl = self.GetUrl.get_attribute("currentSrc")
        self.Browser.get(self.GetUrl)
    #moves song forward by 30sec 
    def MoveForward(self):
        #!Time In Seconds. [ Default 30 Sec ]
        self.Browser.execute_script("document.getElementsByTagName('video')[0].currentTime += %s"%self.IncreaseTime)
    #moves song backward by 30 sec
    def MoveBackwards(self):
        #!Time In Seconds. [ Default : 30 Sec] 
        self.Browser.execute_script("document.getElementsByTagName('video')[0].currentTime += %s"%self.DecreaseTime)
    #restartes the song
    def RestartVideo(self):
        #!Restart Current Video.
        self.CurrentVideoUrl = self.GetUrl
        self.Browser.get(self.CurrentVideoUrl)
        pass
    #pauses the song
    def Pause(self):
        self.Browser.execute_script("document.getElementsByTagName('video')[0].pause()")
        pass
    #resumes the song
    def Play(self):
        self.Browser.execute_script("document.getElementsByTagName('video')[0].play()")
        pass
    #closes application
    def Close(self):
        self.Browser.close()
        win.destroy()
        exit(1)
    


    
x = YoutubeMusic()


    
def ClickAction():
    contentName=songname_text.get()
    songname_text.delete(0,END)
    x.NavigateYoutube(contentName)
    x.ListVideos()
def takenum():
    while True:
        try:
            while True:
                contentchoicenum = int(contentchoice.get())
                print(type(contentchoice.get()))
                contentchoice.delete(0,END)
                if(contentchoicenum == 0):
                    #!If no input is provided regarding music it will take 1st music out of list.
                    x.PlayVideo(1)
                else:
                    x.PlayVideo(contentchoicenum)
        except common.exceptions.ElementClickInterceptedException:
            print("Unknown Error: Please Try Again.")
        except ValueError:
            x.NavigateYoutube(contentName)
            x.ListVideos()
def play():
    self.Browser.execute_script("document.getElementsByTagName('video')[0].play()")
    pass   



#make interface
#create window - title( Media player)
win = Tk()
win.configure(bg = '#900C3F')
win.title('Media Player')

 #buttons - media(open file, open folder , save as, quit), audio(inc volume, dec volume, mute), vedio(play, stop, pause)
menubar = Menu(win)

mediamenu = Menu(menubar,tearoff = 0)
mediamenu.add_command(label = "Open File", command = openfile)
mediamenu.add_command(label = "Open Folder")
mediamenu.add_command(label = "Save As")
mediamenu.add_separator()
mediamenu.add_command(label = "Quit")
menubar.add_cascade(label = "Media", menu = mediamenu)


audiomenu = Menu(menubar, tearoff=0)
audiomenu.add_command(label="Increase Volume")
audiomenu.add_command(label="Decrease Volume")
audiomenu.add_command(label="Mute")
menubar.add_cascade(label="Audio", menu=audiomenu)


win.config(menu=menubar)

#Screen Buttons
songname = Label(win,text = "Song Name",bg = '#c48e9b')
songname.grid(row = 0, column = 0)

songname_text = Entry(win)
songname_text.grid(row = 0, column = 1)
songname_text.insert(END,'Enter song name:')

search = Button(text = "Search Online",padx = 20 , command  = ClickAction).grid(row = 0, column = 2)

search_results = Label(win, text = "Search Results: " , bg = '#c48e9b' ).grid(row = 1, column = 0)

results = Listbox(win, height = 3,width = 40)
results.grid(row = 2, column = 0, rowspan = 4, columnspan = 2)

sb1 = Scrollbar(win)
sb1.grid(row = 2, column = 2, rowspan = 4)
results.configure(yscrollcommand = sb1.set)
sb1.configure(command = results.yview)


contentchoice = Entry(win)
contentchoice.grid(row =7, column = 0)
contentchoice.insert(END,'Enter choice here:')

enter = Button(win,text = "Enter" ,command = takenum).grid(row = 7, column = 1)

#search results

pause = Button(win,text = "Pause", command = x.Pause, width = 12).grid(row=1 ,column = 3)
play = Button(win,text = "play", command = x.Play,width = 12).grid(row= 2,column = 3 )
forward = Button(win,text = "Forward", command = x.MoveForward ,width = 12).grid(row=3 ,column =3 )
backward = Button(win,text = "Backward", command = x.MoveBackwards, width = 12).grid(row=4 ,column = 3)
restart = Button(win,text = "Restart", command = x.RestartVideo, width = 12).grid(row=5 ,column = 3)
close = Button(win,text = "Close", command = x.Close, width = 12).grid(row= 6,column =3 )

#activate
win.mainloop()