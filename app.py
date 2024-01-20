from flask import Flask, send_file, render_template, url_for, redirect, request, send_from_directory
from download import VideoDownload
from urllib.parse import unquote
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

    if request.method == 'POST' and 'video_url' in request.form:
        youtubeUrl = request.form["video_url"]
        video = VideoDownload(youtubeUrl)
        message = video.message
        error_type = video.error_type
        filename = video.filename
        title = video.getTitle()

        video.download_video()
    else:
         message = video.message("Masukan Link Anda")
    return render_template('index.html', error_type=error_type,
                               message = message,
                               title=title,
                               filename=filename)

@app.route('/download/<filename>')
def download_file(filename):
    folder = os.path.join(app.root_path, './static/video')
    return send_from_directory(folder, filename, as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)

