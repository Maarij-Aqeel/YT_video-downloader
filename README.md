This Python script allows you to download YouTube videos or audio files directly to your computer. Using the pytube library, it fetches and lists available streams for a given YouTube link, which can then be downloaded in the desired format.

Features:
Automatic URL Fetching: The script automatically fetches the URL from the clipboard.
Format Selection: Users can choose to download either video or audio.
Stream Listing: Lists all available streams for the selected format.
Easy Downloading: Downloads the selected stream to a specified directory.
Automatic Directory Opening: Opens the download directory upon completion.
Requirements
pytube library
pyperclip library
Usage
Copy the YouTube video URL to your clipboard.
Run the script.
Follow the on-screen prompts to choose between downloading audio or video.
Select the desired stream from the list.
The script will download the file to the specified directory and open it upon completion.
Example
bash
Copy code
$ python YT_video_downloader.py
Note
Make sure to modify the download paths in the script ("E:\\Youtube\\Video" and "E:\\Youtube\\Audio") to match your desired download directories# YT_video-downloader
