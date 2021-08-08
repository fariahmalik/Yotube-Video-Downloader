from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('550x400')
root.resizable(0,0)
root.title("Youtube video downloader")
logo=PhotoImage(file='youtube1.png')
imgLbl = Label(root,image=logo)
imgLbl.place(x=100,y=5)

link = StringVar()

Label(root, text = 'Paste Link Here', font = 'arial 15 bold').place(x= 180 , y = 140)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 60, y = 185)

# Main Function
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.filter(file_extension='mp4',progressive='True').get_by_itag(22)
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

# Button
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'white smoke', padx = 2, command = Downloader).place(x=200 ,y = 250)

root.mainloop()