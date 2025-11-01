from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import yt_dlp
import os

playlist_url="https://www.youtube.com/playlist?list=PL7adgeF1zC0Q1BwNpgYfd8iYL1aYXNH2Z"

driver=webdriver.Chrome()
driver.get(playlist_url)
time.sleep(5)  

videos=[]
video_elements=driver.find_elements(By.XPATH,"//ytd-playlist-video-renderer//a[@id='video-title']")
for v in video_elements:
    title=v.get_attribute("title")
    url=v.get_attribute("href")
    videos.append([title,url])

with open("playlist_videos.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["Title","URL"])
    writer.writerows(videos)

driver.quit()

download_path = r"D:\MyVideos" 
os.makedirs(download_path, exist_ok=True)

ydl_opts={
    'outtmpl':os.path.join(download_path, '%(title)s.%(ext)s'),
    'format':'bestvideo+bestaudio/best',
    'ignoreerrors':True
    }

def progress(d):
    if d['status']=='downloading':
        print(f"Downloading: {d['filename']} {d['_percent_str']} {d['_eta_str']}")
    elif d['status']=='finished':
        print(f"Finished: {d['filename']}")

ydl_opts['progress_hooks']=[progress]

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for _,url in videos:
        print(f"Starting download: {url}")
        ydl.download([url])
