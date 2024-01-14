from pytube import YouTube


def get_title(yt):
    return yt.title


def download_video(yt):
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(22)
    stream.download()

if __name__ == "__main__":
    link = str(input("Insert Link  : "))
    yt = YouTube(link)

    print(get_title(yt))
    download_video(yt)
    
