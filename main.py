from pytube import YouTube
from pydub import AudioSegment
import os
import json

def download_youtube_video_and_convert_to_mp3(url, output_path = "./musics"):  
    # Baixar o vídeo do YouTube  
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    downloaded_file = stream.download(output_path=output_path)

    # Converter o arquivo de áudio para MP3
    base, ext = os.path.splitext(downloaded_file)
    mp3_file = base + ".mp3"
    AudioSegment.from_file(downloaded_file).export(mp3_file, format="mp3")

    # Remover o arquivo de áudio original
    os.remove(downloaded_file)
    return mp3_file

def read_json():
    with open("urls.json", encoding='utf-8') as file:
        data = json.load(file)
        return data["urls"]

try:
    for url in read_json():        
        mp3_file = download_youtube_video_and_convert_to_mp3(url)
        print(f"O arquivo MP3 foi salvo em: {mp3_file}")
except Exception:
    print("Falha ao realizar conversão")