#!/usr/bin/env python3
import yt_dlp
import argparse
import os

# 1. Configuração de caminhos robusta
home_path = os.path.expanduser("~")
downloads_path = os.path.join(home_path, "Downloads")

# Garante que a pasta existe no Kali/Linux
if not os.path.exists(downloads_path):
    os.makedirs(downloads_path, exist_ok=True)

parser = argparse.ArgumentParser(
    prog="ytdl",
    description="Simple YouTube downloader CLI"
)

parser.add_argument("-u", "--url", help="URL da música ou vídeo")
parser.add_argument("-f", "--file", help="Arquivo contendo URLs")
parser.add_argument("-o", "--output", help="Diretório de destino")

args = parser.parse_args()

# Define local de saída usando o separador correto do SO
final_output = args.output if args.output else downloads_path
output_template = os.path.join(final_output, '%(title)s.%(ext)s')

opcoes = {
    'format': 'bestaudio/best',
    'quiet': False, # Coloque True se quiser um terminal limpo
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': output_template
}

def executar_download(link):
    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([link.strip()])
    except Exception as e:
        print(f"Erro no link {link}: {e}")

if args.url:
    executar_download(args.url)
elif args.file:
    if os.path.exists(args.file):
        with open(args.file, 'r') as arquivo:
            for linha in arquivo:
                if linha.strip():
                    executar_download(linha)
    else:
        print("Arquivo de lista não encontrado.")
else:
    parser.print_help()