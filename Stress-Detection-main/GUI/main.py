import streamlit as st
import os
from PIL import Image
import pandas as pd
from io import StringIO

import pydub
from pathlib import Path
from typing import List
import asyncio

flag = 0


st.title('Stress Detection System')


async def upload_and_save_wavfiles(save_dir: str) -> List[Path]:
    uploaded_files = st.file_uploader("upload", type=['wav', 'mp3'], accept_multiple_files=True)
    save_paths = []
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            if uploaded_file.name.endswith('wav'):
                audio = pydub.AudioSegment.from_wav(uploaded_file)
                file_type = 'wav'
            elif uploaded_file.name.endswith('mp3'):
                audio = pydub.AudioSegment.from_mp3(uploaded_file)
                file_type = 'mp3'

            # Change the file name here (example: appending '_renamed' to the original name)
            new_filename = f"aud.{file_type}"
            save_path = Path(save_dir) / new_filename

            save_paths.append(save_path)
            audio.export(save_path, format=file_type)
            flag = 1
    return save_paths


def display_wavfile(wavpath):
    audio_bytes = open(wavpath, 'rb').read()
    file_type = Path(wavpath).suffix
    st.audio(audio_bytes, format=f'audio/{file_type}', start_time=0)

async def daaa():
    path = await upload_and_save_wavfiles('data')
    if path:
       display_wavfile('data/aud.wav')
    print(path)
    if path:  # Check if files list is not empty
        import data_analysis
        print(path)
        data_analysis.func('data/aud.wav')
    else:
        print("No files uploaded or processed.")

asyncio.run(daaa())
