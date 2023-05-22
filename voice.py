import os
import openai

audio_file = open("german.m4a", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)