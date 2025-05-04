from yt_dlp import YoutubeDL

def main():
    is_running = True
    yt_url = input("Enter youtube URL here: ")
    while is_running:
        if "https://www.youtube.com" not in yt_url:
            print("Invalid URL, try again")
            yt_url = input("Enter youtube URL here: ")
        else:
            is_running = False

    quality = input("Which mp3 quality do you want to download (128kbps,192kbps,320kbps): ")
    while is_running:
        if quality == "128" or quality =="192" or quality =="320":
            is_running = False
        else:
            print("Invalid quality, try again")
            quality = input("Which mp3 quality do you want to download (128kbps,192kbps,320kbps): ")


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