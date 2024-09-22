import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("MP3 MUSIC PLAYER")
root.geometry("485x700+290+10")
root.configure(background="BLACK")
root.resizable(False,False)
mixer.init()

lower_frame = Frame(root, background= "white",width= 485 , height=180)
lower_frame.place(x=0,y=400)

frameCnt = 10
frames = [PhotoImage(file= "gif.gif",format = 'gif - %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

def Addmusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END,song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

Menu = PhotoImage("menu.png")
Label(root,image=Menu).place(x=0, y=580, width=485,height=100)

Frame_music = Frame(root, bd=2, relief= RIDGE)
Frame_music.place(x=0, y=580, width=485,height=100)

Button(root, text = "Browse Music", width=59, height=1, font= ("calibri",12,"bold"), fg="Black",bg="White",command= Addmusic).place(x=0,y=550)


# Button
ButtonPlay = PhotoImage(file="play1.png")
Button(root, image=ButtonPlay, bg="blue", bd=0, height = 60, width =60,command=PlayMusic).place(x=215, y=487)

ButtonStop = PhotoImage(file="stop1.png")
Button(root, image=ButtonStop, bg="black", bd=0, height = 60, width =60,command=mixer.music.stop).place(x=130, y=487)

Buttonvolume = PhotoImage(file="volume.png")
Button(root, image=Buttonvolume, bg="green", bd=0, height = 60, width =60,command=mixer.music.unpause).place(x=20, y=487)

ButtonPause = PhotoImage(file="pause1.png")
Button(root, image=ButtonPause, bg="red", bd=0, height = 60, width =60,command=mixer.music.pause).place(x=300, y=487)


Scroll = Scrollbar()
Playlist = Listbox(Frame_music,width=100,font=("Times new roman",10), bg="black",fg="grey",selectbackground="Lightblue",cursor = "hand2",bd = 0,yscrollcommand= Scroll.set)

Scroll.config(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill = Y)
Playlist.pack(side = RIGHT, fill = BOTH)

root.mainloop()  