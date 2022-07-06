import pytube
url = "https://www.youtube.com/shorts/fLkMi-FPgOQ"#input('Enter here the Link: ')
youtube = pytube.YouTube(url)
sound = youtube.streams.get_audio_only()
sound.download()