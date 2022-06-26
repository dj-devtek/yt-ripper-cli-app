# yt-ripper-cli-app
Command line interface application for automating the process of ripping audio from Youtube videos.

Online Youtube to mp3 converters are slow and often do not set the correct meta data for easy import into DJ softwares as Serato. This application allows you to set the meta data during the download process, resulting in quick audio ripping and formatting.

**Disclaimer:** YouTube audio is compressed using ACC when uploaded. This means that the highest quality anyone can rip from YouTube is around 128kbps. In some cases it can be as high as 256kbps. This application rips the highest possible audio quality from the selected videos.

## Important
This CLI application was built, tested, and verified to work on a Mac OS operating system. There is no gaurentee it will work with Linux, Windows, etc... The following instructions are meant for Mac users.

## Clone repository
Pull down code to your local computer using the following command...
```
git clone https://github.com/dj-devtek/yt-ripper-cli-app.git
```

## Prerequisites
The python script uses the os library to run system commands on the host operating system. You will need to be running python3. Also, you must ffmpeg(audio extractor) and youtube-dl installed before you continue.

To check your python version, run...
```
python3 --version
```
To install youtube-dl, run...
```
brew install youtube-dl
```
To install ffmpeg, run...
```
brew install ffmpeg
```

## Running the app
navigate to the folder which you cloned the repository code and run...
```
python3 dj-rip.py
```
From here, you can choose to download a single song or multiple from a list

### Rip single song
To rip a single song audio from youtube, enter 1 and fill in the prompts (youtube link, song name, song artist). The download should then start

### Rip from file
To rip multiple songs in a row, you must first create a text file in the same directory and format it to include song information. Upon cloning the repositor, there should be a default file named **songs.txt**. Fill this file with the song information.

Each line of songs.txt must be in the following format: [youtube link]-[song title]-[song artist]

after running dj-rip.py, enter 2, followed by **songs.txt** for the "Rip Filename" prompt.

## Finishing up
All ripped audio should be in your downloads folder
