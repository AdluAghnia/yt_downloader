from flask import Flask, send_file, render_template, url_for, redirect, request
from download import download_video
from pytube import YouTube
from pathlib import Path
import re
import os
app = Flask(__name__)

@app.route("/")
def index():
    """
    Ini Fungsi Buat Halaman Utama
    """

    return render_template("index.html")


@app.route("/download", methods = ['GET', 'POST'])
def download():
    """
    Fungsi ini untuk mendownload video dan memasukannya ke static file
    """
    message = ''
    error_type = 0
    if request.method == 'POST' and 'video_url' in request.form:
        youtubeUrl = request.form["video_url"]
        if youtubeUrl:
            validateVideoUrl = (
                r'(https?://)?(www\.)?'
                '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
            )

            validateVideoUrl = re.match(validateVideoUrl, youtubeUrl)

            if validateVideoUrl:
                url = YouTube(youtubeUrl)
                video = url.streams.get_highest_resolution()
                download_folder = r"./static/vid_downloaded/"
                title = video.title

                video.download(download_folder)
                message = "Video Telah Berhasil Di Download"
                error_type = 1
            else:
                message = "Masukan Link Yang Valid"
                error_type = 0
        else:
            message = "Masukakn Link Anda"
            error_type = 0

        return render_template('index.html', error_type=error_type,
                               message = message,
                               title=title)
if __name__ == "__main__":
    app.run(debug=True)

