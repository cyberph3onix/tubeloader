from yt_dlp import YoutubeDL
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="to download the video")
parser.add_argument("-a","--audio", help="to download only the audio", action='store_true')

args = parser.parse_args()

ydl_opts = {}

if args.audio:
   ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{ 
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

with YoutubeDL(ydl_opts) as ydl: #if -a is not used then the default ydl_opts={} will run
   ydl.download(args.url)

