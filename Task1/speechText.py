import speech_recognition as sr
filename=""
r=sr.Recognizer()
with sr.AudioFile(filename) as source:
	audio_data = r.record(source)
	text=r.recognize_google(audio_data)