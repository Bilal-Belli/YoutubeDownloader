import pytube
url = "https://www.youtube.com/watch?v=sc9NFJ-LrCk&list"#input('Enter here the Link: ')
youtube = pytube.YouTube(url)


video = youtube.streams.get_highest_resolution()
video.download()