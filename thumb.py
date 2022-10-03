import streamlit as st
import requests
from pytube import YouTube, extract
from os import makedirs

def format_title(title):
    new_title = ''
    for ch in title:
        if ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_()[]{} ':
            new_title += ch
    return new_title


st.title('YouTube Thumbnail Downloader')

url = st.text_input('Enter the URL of the video:')

if st.button('Download Thumbnail'):
    yt_fomatted_title = format_title(YouTube(url).title)

    yt_id = extract.video_id(url)

    makedirs('Thumbnails', exist_ok=True)
    yt_thumbnail = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
    r = requests.get(yt_thumbnail, allow_redirects=True)
    open(f'Thumbnails\\{yt_fomatted_title}.jpg', 'wb').write(r.content)

    st.image(yt_thumbnail)

    st.success('Thumbnail downloaded successfully (by FHDP)')

    # https://youtu.be/T611mVOrPQg
