from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from distutils.command.sdist import sdist
from ossaudiodev import SNDCTL_SEQ_CTRLRATE
import ssl
from this import s
import pytube
url = "https://www.youtube.com/watch?v=sc9NFJ-LrCk&list"#input('Enter here the Link: ')
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()