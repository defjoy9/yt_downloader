# YouTube to MP3 Converter (CLI Tool)

A simple Python script that converts YouTube videos to high-quality audio files (MP3, Opus, or M4A) using `yt-dlp` and `ffmpeg`.

## 📦 Requirements

- Python 3.10+ (recommended: 3.11)
- `yt-dlp==2025.4.30`
- `ffmpeg` installed and available in your system's PATH

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage
Run the script
```bash
python main.py
```
Then follow the prompts:

    Enter the YouTube video URL

    Choose audio codec (mp3, opus, m4a)

    Select desired quality (128, 192, or 320)

The audio file will be downloaded and saved in the current directory.

## Example

    Enter YouTube URL here: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Which codec to use (mp3, opus, m4a): mp3
    Which audio quality do you want (128, 192, 320 kbps): 320
File will be saved with the video title as the filename (e.g., Some_Song_Title.mp3).

## License
This project is licensed under the MIT License.