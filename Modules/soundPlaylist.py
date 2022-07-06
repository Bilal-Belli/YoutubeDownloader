import pytube
from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLIbbPnzLyFER3f-Cg9VEU7mGVwGhDx6H_')
print(f'Downloading: {p.title}')
for video in p.videos:
    print(video.title)
    st = video.streams.get_audio_only()
    st.download()