import yt_dlp
import argparse
import os

# cria parser CLI
parser = argparse.ArgumentParser(
    prog="ytdl",
    description="Simple YouTube downloader CLI made with Python"
)

# argumento URL
parser.add_argument(
    "-u",
    "--url",
    help="URL da música ou vídeo"
)

# argumento arquivo/wordlist
parser.add_argument(
    "-f",
    "--file",
    help="Arquivo contendo URLs"
)

# argumento diretório de download
parser.add_argument(
    "-o",
    "--output",
    help="Diretório onde os downloads serão salvos"
)

# pega argumentos
args = parser.parse_args()

# pega pasta Downloads do Windows
downloads_path = os.path.join(
    os.path.expanduser("~"),
    "Downloads"
)

# local padrão
output_path = f'{downloads_path}/%(title)s.%(ext)s'

# se usuário escolher outro diretório
if args.output:
    output_path = f'{args.output}/%(title)s.%(ext)s'

# opções yt-dlp
opcoes = {
    'format': 'bestaudio/best',

    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],

    'outtmpl': output_path
}

# inicia yt-dlp
with yt_dlp.YoutubeDL(opcoes) as ydl:

    # download URL única
    if args.url:
        ydl.download([args.url])

    # download wordlist
    elif args.file:

        with open(args.file, 'r') as arquivo:

            urls = arquivo.readlines()

            for url in urls:
                ydl.download([url.strip()])

    # caso usuário não use argumentos
    else:
        print("Use -u para URL ou -f para arquivo")