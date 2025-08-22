from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError
import urllib as lib
import requests as resq

yt = YouTube('https://pornez.net/video860883/trueanal-taking-scarlett-hamptons-ass-for-a-ride-mikea-1080p-ode/')

yt.streams.filter(progressive=True,
    file_extension='mp4').order_by('resolution')[-1].download()
