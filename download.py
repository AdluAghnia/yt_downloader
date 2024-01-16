from pytube import YouTube

def download_video(yt, save_path : str, url : str):
    """
    Fungsi ini untuk mendownload video dan memasukannya ke static file
    """
    try:
        yt.streams.filter(file_extension='mp4')
        stream = yt.streams.get_by_itag(22)
        stream.download(output_path=save_path)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    download_video("./statics/vid_downloaded", "https://youtu.be/_xXGj-h4nto?si=AfnvKC-1ZC75Eb5D")
   
