import nltk
#nltk.download('averaged_perceptron_tagger')
s="i have cancer and high blood pressure"
#s=s.lower()
tokens = nltk.word_tokenize(s)
tagged = nltk.pos_tag(tokens)
tagged=dict(tagged)
print(tagged)
words={"positive":["have","suffer","got","diagnose"],"negative":["no","not","don't","do not"]}
options=["thyroid","cancer","others","none","diabetes"]
ans=[]
s1=[]
var=0
t=0
for i in tokens:
	if (i in words["positive"]) or (i in words["negative"]) or (i in options) or (tagged[i]=="NN"):
		s1.append(i)
print(s1)
for i in range(0,len(s1)):
	if s1[i] not in words["positive"] and s1[i] not in words["negative"]:
		ans.append(s1[i])
		s1.remove(s1[i])
		i+=1
	else:
		break
for i in s1:
	if i in words["positive"] and t==0:
		var=1
		continue
	if i in words["negative"]:
		var=-1
		t+=1
		continue
	if var==1:
		t=0
		ans.append(i)
		continue
	t=0
t=0
r=[]

for i in ans:
	if i not in options:
		t+=1
		r.append(i)
for i in r:
	ans.remove(i)
'''
for i in range(0,len(ans)):
	if ans[i] not in options:
		t+=1
		ans.remove(ans[i])
		i+=1
'''
if "others" in options and t>0:
	ans.append("Others")
if "none" in options and len(ans)==0:
	ans.append("None")

print(ans)