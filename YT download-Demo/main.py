from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
import os

main_bg = "#181818"
second_bg = "#202020"

root=Tk()
root.title('YT Download')
root.geometry('925x500+300+200')
root.configure(bg=main_bg)
root.resizable(False,False)
photo = PhotoImage(file="YT download-Demo/yt.png")
root.iconphoto(False, photo)

heading=Label(text='YT Downloader',fg='white',bg=main_bg,font=("Microsoft YaHei UI Light",21,'bold'))
heading.place(x=350,y=20)
text2=Label(text='Convert and download YouTube audio online, for free.',fg='white',bg=main_bg,font=("Roboto",12))
text2.place(x=280,y=70)

frame=Frame(root,width=600,height=80,bg=second_bg)
frame.place(x=170,y=120)

frame2=Frame(root,width=600,height=200,bg=second_bg)
frame2.place(x=170,y=250)
success_list = []

txt_output = Text(frame2, height=10,border=0, width=72,bg=second_bg,fg="white")
txt_output.place(x=10,y=30)

txt_directory = Label(text="" ,bg=main_bg,fg="white",font=("Roboto",12))
txt_directory.place(x=245,y=210)

def clear_list():
    success_list.clear()
    txt_output.delete("1.0","end")
    
clear_btn = Button(frame2,width=10,text='clear history',border=0,bg=second_bg,cursor='hand2',fg="white",command=clear_list)
clear_btn.place(x=510,y=5)

def select_folder():
   path= filedialog.askdirectory(title="Select a Folder")
   txt_directory.configure(text = path)

# Create a label and a Button to Open the dialog
button = Button(root, text="Save to",height=1,width=6, bg="white",fg="black",border=0 , command=select_folder)
button.place(x=185,y=210)

def convert():
    #txt_waiting.configure(text="downloading...")
    link_convert = link.get()
    yt = YouTube(link_convert)
    video = yt.streams.filter(only_audio=True).first()
    destination = txt_directory.cget('text')

    out_file = video.download(output_path=destination)
  
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
  
    print(yt.title + " has been successfully downloaded.")
    success_list.append("=> " + yt.title + " ✅")
    for item in success_list:
        txt_output.insert(END, item + "\n")
    success_list.clear()
    #txt_waiting.configure(text=" ")

def on_enter(e):
    link.delete(0, 'end')

def on_leave(e):
    name=link.get()
    if name == '':
        link.insert(0, 'Past youtube link here')

link = Entry(frame,width=40,fg="white",border=0,bg=main_bg,font=("Microsoft YaHei UI Light",14))
link.place(x=30,y=25)
link.insert(0,'Past youtube link here')
link.bind('<FocusIn>', on_enter)
link.bind('<FocusOut>', on_leave)

Button(frame,width=10,pady=7,text='convert',bg='#57a1f8',fg='white',border=0,command=convert).place(x=500,y=23)

root.mainloop()
