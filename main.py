from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Vikedi Host Technology")
root.configure(background='white')
Label(root,text = 'Youtube Video Downloader', font ='arial 17 bold').pack()
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 12 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70, textvariable = link, bg = '#e33e32', fg='white' ).place(x = 32, y = 90)
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 10 bold' ,bg = '#e33e32', fg='white', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()