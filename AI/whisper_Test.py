"""
pip install pytube
pip install ffmpeg-python
brew install ffmpeg
pip install git+https://github.com/openai/whisper.git
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
pip install setuptools-rust
"""
# import model1 as model1
# import pytube
# # Reading the above Taken movie Youtube link
# video = "https://www.youtube.com/watch?v=-LIIf7E-qFI"
# data = pytube.YouTube(video)
# # Converting and downloading as 'MP4' file
# audio = data.streams.get_audio_only()
# audio.download()

# Installing Whisper libary


import whisper
model = whisper.load_model("base")
result = model.transcribe("aa.mp4")
print(result["text"])

