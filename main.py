from yt_dlp import YoutubeDL

def main():
    # user enters youtube URL
    yt_url = input("Enter youtube URL here: ")
    while "https://www.youtube.com/" not in yt_url:
        yt_url = input("Invalid URL, try again: ")

    # user selects desired quality
    quality = input("Which mp3 quality do you want to download (128kbps,192kbps,320kbps): ")
    while quality not in ("128", "192", "320"):
        quality = input("Invalid quality, try again (128/192/320): ")

    # setting up all the required options to download URL
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality
}]}
    # converting audio to mp3 and saves the {codec} file.
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
    except Exception as error:
        print(f"WARNING! AN EXCEPTION OCURRED: {error}")

if __name__ == "__main__":
    main()