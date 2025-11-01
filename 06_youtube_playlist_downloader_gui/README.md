## Project Overview

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium&logoColor=white) ![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-orange) ![FFmpeg](https://img.shields.io/badge/FFmpeg-required-red)

This project demonstrates **automated YouTube playlist scraping and video downloading using Selenium and yt-dlp**. It scrapes video titles and URLs from a playlist, saves the list into a CSV file, and downloads each video with best video and audio quality.

### Features

- Open a YouTube playlist using Selenium.
- Scrape all video titles and URLs from the playlist.
- Save video details into `playlist_videos.csv`.
- Download videos using yt-dlp in best video + audio format.
- Show download progress and completion messages in terminal.

### Setup & Usage

1. **Install Python 3.11+** if not already installed.

2. **Check for FFmpeg**  
   Open a terminal or command prompt and run:

   ```bash
   ffmpeg -version
   ```

   - If FFmpeg is installed, you will see version info.
   - If not installed, download and install from [FFmpeg official site](https://ffmpeg.org/download.html) and ensure it's added to your system PATH.
   - Check again:
     ```bash
     ffmpeg -version
     ```

3. **Install required Python packages**

```bash
   pip install selenium yt-dlp webdriver-manager

```

4. **Provide a Youtube Playlist URL (Must be Publicly Avalable)**
   in the main.py - in playlist_url provide your playlist_url link
   ```python
   playlist_url="playlist-url"
   ```
5. **Run the script**
   Navigate to the project folder and execute:

```bash
  python main.py
```

5. **Outputs**
   - `playlist_videos.csv` containing all video titles and URLs.
   - Downloaded videos in the same directory with best video + audio quality.

### Notes

- Make sure your internet connection is stable for downloading videos.
- Adjust playlist URL in `main.py` to scrape different playlists.
- For large playlists, downloads may take longer depending on video size.

```

```
