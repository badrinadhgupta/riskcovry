import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()
file_audio = sr.AudioFile('Recording (3).wav')

with file_audio as source:
   audio_text = r.record(source)

s = r.recognize_google(audio_text)
s = s.split(' ')
options = ["<5lakh", "5lakh-15lakh", '15lakh-20lakh', '20lakh>']

req = ''
for j in s:
   if ord(j) in range(48, 57):
      req += j
lt, gt = 0, 0
cur_num = ''
r1, r2 = '', ''
d = 0
ans = ''
for i in range(len(options)):
   if '<' in options[i]:
      lt = 1
      for j in options[i]:
         if ord(j) in range(48, 57):
            cur_num+= j
   elif '>' in options[i]:
      gt = 1
      for j in options[i]:
         if ord(j) in range(48, 57):
            cur_num+= j
   else:
      for j in options[i]:
         if ord(j) in range(48, 57) and d==0:
            r1+=j
         if j=='-':
            d=1
         if ord(j) in range(48, 57) and d==1:
            r2+=j
   if lt==1:
      if int(req) < int(cur_num):
         ans = options[i]
         break
   if gt==1:
      if int(req) >= int(cur_num):
         ans = options[i]
         break
   if d==1:
      if int(r1)<=int(req) and int(r2)>int(req):
         ans = options[i]

   lt, gt, d = 0, 0, 0
   r1, r2 = '', ''
   cur_num = ''

print(ans)

