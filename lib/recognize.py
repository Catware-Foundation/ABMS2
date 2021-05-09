
def recongnize(link):
    download(str(link), "file.mp3")
    sound = AudioSegment.from_mp3("file.mp3")
    sound.export("file.wav", format="wav")
    sample_audio = speech_recog.AudioFile('file.wav')

    with sample_audio as audio_file:
        audio_content = rec.record(audio_file)
        txt = rec.recognize_google(audio_content, language="ru-RU")

    return txt

def recongnize_local(path):
    sound = AudioSegment.from_mp3(str(path))
    sound.export("file.wav", format="wav")
    sample_audio = speech_recog.AudioFile('file.wav')

    with sample_audio as audio_file:
        audio_content = rec.record(audio_file)
        txt = rec.recognize_google(audio_content, language="ru-RU")

    return txt
  
#
# Не тестировалось!
#
