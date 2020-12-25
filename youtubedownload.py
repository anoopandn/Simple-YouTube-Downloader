from pytube import YouTube
link=input("enter the url: ")
YouTube(link).streams.first().download()
print("successfully")