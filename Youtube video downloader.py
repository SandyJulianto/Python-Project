# Youtube Video Downloader
# Import modules
from pytube import YouTube

# Save location
SAVE_PATH = C;

# Download links
link = input("Enter YouTube Link\n")
yt = YouTube(link)

# Video details 
print("Title : {}".format(yt.title))
print("Views : {}".format(yt.views))
print("Length : {}".format(yt.length))

# Get highest resolution possible
yt_res = yt.streams.get_highest_resolution()

# Downloading
try:
    yt_res.download()
except:
    print("Link error")

print("Download Completed")



    