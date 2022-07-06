import pytube
url = "https://www.youtube.com/shorts/fLkMi-FPgOQ"#input('Enter here the Link: ')
youtube = pytube.YouTube(url)
video = youtube.streams.get_lowest_resolution()
video.download()