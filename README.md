# ytdl-cli

Simple YouTube downloader CLI made with Python.

## Features

- Download music from YouTube
- Batch download using wordlists
- Automatic MP3 conversion
- Custom output directory
- CLI arguments support

## Requirements

- Python 3
- ffmpeg
- yt-dlp

## Installation

Install yt-dlp:

```bash
pip install yt-dlp
```
## FFmpeg Installation

### Windows (Chocolatey)

Install Chocolatey:

https://community.chocolatey.org/

Then install FFmpeg:

```powershell
choco install ffmpeg
```

Restart the terminal after installation.

Test:

```powershell
ffmpeg -version
```

---

### Linux (Debian/Ubuntu)

```bash
sudo apt install ffmpeg
```
## Usage

### Download a single video/music

```bash
python ytdl.py -u URL
```

Example:

```bash
python ytdl.py -u https://youtu.be/example
```

---

### Download from a wordlist

Create a text file:

```text
https://youtu.be/link1
https://youtu.be/link2
https://youtu.be/link3
```

Run:

```bash
python ytdl.py -f wordlist.txt
```

---

### Custom output directory

```bash
python ytdl.py -u URL -o Downloads
```

---

### Help menu

```bash
python ytdl.py -h
```

## Example

```bash
python ytdl.py -u https://youtu.be/example -o Musicas
```

## Author

Made with Python for learning purposes.