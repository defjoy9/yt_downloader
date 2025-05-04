from yt_dlp import YoutubeDL

def main():
    yt_url = input("Enter youtube URL here: ")
    while "https://www.youtube.com/" not in yt_url:
        yt_url = input("Invalid URL, try again: ")

    quality = input("Which mp3 quality do you want to download (128kbps,192kbps,320kbps): ")
    while quality not in ("128", "192", "320"):
        quality = input("Invalid quality, try again (128/192/320): ")


    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s_opus.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality
}]}

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])


if __name__ == "__main__":
    main()