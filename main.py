from yt_dlp import YoutubeDL

def main():
    # user enters youtube URL
    yt_url = input("Enter youtube URL here: ")
    while "https://www.youtube.com/" not in yt_url:
        yt_url = input("Invalid URL, try again: ")
    
    #user chooses desired codec
    codec = input("Which codec to use (mp3,opus,m4a): ")
    while codec not in ("mp3","opus","m4a"):
        codec = input("Invalid codec, try again (mp3,opus,m4a): ")
    
    # user selects desired audio quality
    quality = input(f"Which {codec} quality do you want to download (128kbps,192kbps,320kbps): ")
    while quality not in ("128", "192", "320"):
        quality = input("Invalid quality, try again (128/192/320): ")

    # yt-dlp configuration options for audio extraction
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': quality
}]}
    # download and convert audio using yt-dlp
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
    except Exception as error:
        print(f"WARNING! AN EXCEPTION OCURRED: {error}")

if __name__ == "__main__":
    main()