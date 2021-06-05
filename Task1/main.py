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
        options = eval(request.args.get("options"))
        baudio = bytes(audio, 'utf-8')
        decode_string = base64.b64decode(baudio+b"==")
        ogg_file = open("temp.ogg", "wb")
        ogg_file.write(decode_string)
        ogg_file1 = open("temp.ogg", "rb")
        return callSpecificQuestion(ogg_file1,question_key,options)
    def post(self):
        audio = request.json.get("audio")
        question_key = request.json.get("question_key")
        options = request.json.get("options")
        baudio = bytes(audio, 'utf-8')
        decode_string = base64.b64decode(baudio+b"==")
        ogg_file = open("temp.ogg", "wb")
        ogg_file.write(decode_string)
        ogg_file1 = open("temp.ogg", "rb")
        return callSpecificQuestion(ogg_file1,question_key,options)

    
    
    
@app.route('/form', methods=['GET','POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        audio = request.files.get("audio")
        print(audio)
        question_key = request.form.get("question_key")
        options = eval(request.form.get("options"))
        answer = callSpecificQuestion(audio,question_key,options)
        return '''
                  <h1>{}</h1>'''.format(answer)

    # otherwise handle the GET request
    return '''
           <form method="POST" enctype="multipart/form-data">
           <label for="fname">Question Key:</label>
  <input type="text" id="question_key" name="question_key" value=""><br><br>
  <label for="fname">Options:</label>
  <input type="text" id="options" name="options" value=""><br><br>
  <label for="img">Upload audio file:</label>
  <input type="file" id="audio" name="audio" accept="audio/*"><br><br>
  <input type="submit" value="Submit">
</form> 
           </form>'''

def callSpecificQuestion(audio,question_key,options):
    data, samplerate = sf.read(audio)
    sf.write('temp.wav', data, samplerate)
    r=sr.Recognizer()
    read_file = open("temp.wav", "rb")
    with sr.AudioFile(read_file) as source:
        audio_data = r.record(source)
        t=r.recognize_google(audio_data)
        print(t)
        if(question_key=="q1"):
            return {"answers":q1(t,options)}
        elif(question_key=="q2"):
            return {"answers":q2(t,options)}
        elif(question_key=="q3"):
            return {"answers":q3(t,options)}
        else:
            return {"error":"Correct Question key was not provided"}

api.add_resource(ApiCalls, '/')


if __name__ == '__main__':
    app.run(debug=True)


app.run()


