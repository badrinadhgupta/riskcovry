from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
import speech_recognition as sr
import base64
import soundfile as sf
from q1 import q1
from q2 import q2
from q3 import q3

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
api = Api(app)

class CommandException(Exception):
    """Exception that is raised if calling an external command fails"""
    def __init__(self, command):
        self.command = command
    def __str__(self):
        return self.command


class ApiCalls(Resource):
    def get(self):
        audio = request.args.get("audio")
        question_key = request.args.get("question_key")
        options = request.args.get("options")
        baudio = bytes(audio, 'utf-8')
        decode_string = base64.b64decode(baudio+b"==")
        ogg_file = open("temp.ogg", "wb")
        ogg_file.write(decode_string)
        data, samplerate = sf.read('temp.ogg')
        sf.write('temp.wav', data, samplerate)
        r=sr.Recognizer()
        read_file = open("temp.wav", "rb")
        with sr.AudioFile(read_file) as source:
            audio_data = r.record(source)
            t=r.recognize_google(audio_data)
            t=r.recognize_google(audio_data)
            if(question_key=="q1"):
                return {"asnwers":q1(t,options)}
            elif(question_key=="q2"):
                return {"asnwers":q2(t,options)}
            elif(question_key=="q3"):
                return {"asnwers":q3(t,options)}
            else:
                return {"error":"Correct Question key was not provided"}

api.add_resource(ApiCalls, '/')


if __name__ == '__main__':
    app.run(debug=True)

def helloWorld():
  return "Hello, cross-origin-world!"

app.run()


