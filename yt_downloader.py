from yt_dlp import YoutubeDL
from simple_term_menu import TerminalMenu

def main():
    yt_url = input("Enter youtube URL here: ")
    while "https://www.youtube.com/" not in yt_url:
        yt_url = input("Invalid URL, try again: ")
    
    codec_optkns = ["mp3","opus","m4a"]
    print("Select desired audio codec:")
    terminal_menu = TerminalMenu(codec_optkns)
    menu_entry_index = terminal_menu.show()
    codec = codec_optkns[menu_entry_index]
    print(f"You have selected {codec}!")

    quality_options = ["128kbps", "192kbps", "320kbps"]
    print("Select desired audio quality:")
    terminal_menu = TerminalMenu(quality_options)
    menu_entry_index = terminal_menu.show()
    quality = quality_options[menu_entry_index].replace("kbps","")
    print(f"You have selected {quality_options[menu_entry_index]}!")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': quality
}]}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
    except Exception as error:
        print(f"WARNING! AN EXCEPTION OCURRED: {error}")

if __name__ == "__main__":
    main()