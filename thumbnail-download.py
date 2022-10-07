from pytube import YouTube, extract
from os import system as cmd
from os import makedirs
import requests
from shutil import rmtree
from re import sub


def format_title(title):
    new_title = ''
    for ch in title:
        if ch in 'aáàâãäåbcçdeéèêëfghiíìîïjklmnoóòôõöpqrstuúùûüvwxyzAÁÀÂÃÄÅBCÇDEÉÈÊËFGHIÍÌÎÏJKLMNOÓÒÔÕÖPQRSTUÚÙÛÜVWXYZ0123456789-_()[]{}# ':
            new_title += ch
    new_title = sub(' +', ' ', new_title)
    new_title = new_title.strip()
    return new_title


continue_or_exit = None
while continue_or_exit != '1':
    cmd('cls')

    print()
    yt_url = input('YouTube URL: ')

    yt_fomatted_title = format_title(YouTube(yt_url).title)
    yt_id = extract.video_id(yt_url)
    yt_thumbnail = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'

    # Downloading thumbnail
    makedirs('Thumbnails', exist_ok=True)
    r = requests.get(yt_thumbnail, allow_redirects=True)
    open(f'Thumbnails\\{yt_fomatted_title}.jpg', 'wb').write(r.content)

    # Deleting temporary files
    rmtree('.temp', ignore_errors=True)

    print()

    continue_or_exit = input('[X] Press 1 to exit or any other key to continue ')
