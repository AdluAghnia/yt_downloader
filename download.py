from pytube import YouTube
import re
import string
import random

def generate_random_string():
    # Define the set of characters from which the string will be composed
    characters = string.ascii_letters + string.digits

    # Generate a random string of length 5
    random_string = ''.join(random.choice(characters) for _ in range(5))

    return random_string

class VideoDownload:
    def __init__(self, link):
        self.link = link
        self.message = ''
        self.error_type = 0
        self.filename = generate_random_string()+'.mp4'
        if self.validateVideoUrl():
            self.url = YouTube(self.link)
            self.error_type = 1
        else:
            self.message = "Link yang anda masukan tidak valid"
    
    def validateVideoUrl(self):
        validateVideoUrl = (
                    r'(https?://)?(www\.)?'
                    '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                    '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
                )
        validateVideoUrl = re.match(validateVideoUrl, self.link)

        return validateVideoUrl

    def getTitle(self) -> str:
        return self.url.title
    
    def download_video(self):
        download_folder = "./static/video/"
        video =  self.url.streams.get_lowest_resolution()

        if video:
            video.download(download_folder, filename=self.filename)
        else:
            print("None")

if __name__ == "__main__":
    print(generate_random_string())