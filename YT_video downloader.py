from pytube import YouTube
import os
import pyperclip

print("This is the YOUTUBE video/audio downloader\n")
url=pyperclip.paste()
link= str(url)



youtube_1=YouTube(link)
print("Title: ",youtube_1.title)
print("Link = ",url)

ask=int(input('\n1:-  Audio\n2:-  Video\n'))
    
print("Searching...")
if ask==2:

    videos=youtube_1.streams.all()

    vid=list(enumerate(videos))

    for i in vid:
     print(i)
    print()

    strm=int(input("Enter:  "))
    print ("Downloading...")

    videos[strm].download("E:\Youtube\Video")

    print("Succesfully downloaded.")
    os.startfile(r"E:\Youtube\Video")

elif ask==1:

    videos=youtube_1.streams.filter(only_audio=True)
    vid=list(enumerate(videos))

    for i in vid:
     print(i)
    print() 

    strm=int(input("Enter:  "))
    print ("Downloading...")


    videos[strm].download("E:\Youtube\Audio")

    print("Succesfully downloaded")
    os.startfile(r"E:\Youtube\Audio")
