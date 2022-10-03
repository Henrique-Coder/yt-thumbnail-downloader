import streamlit as st
from pytube import YouTube, extract

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

    yt_thumbnail = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'

    st.image(yt_thumbnail)

    st.success('The thumbnail was generated successfully! (Coder: FHDP)')
