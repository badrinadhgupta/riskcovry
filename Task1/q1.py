import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
def q1(s, options):
    s="cancer, high blood pressure"
    #s=s.lower()
    tokens = nltk.word_tokenize(s)
    tagged = nltk.pos_tag(tokens)
    tagged=dict(tagged)
    
    words={"positive":["have","suffer","got","diagnose"],"negative":["no","not","don't","do not"]}
    options=["thyroid","cancer","others","none","diabetes", 'high blood pressure']
    ans=[]
    s1=[]
    var=0
    t=0
    
    for i in tokens:
    	if (i in words["positive"]) or (i in words["negative"]) or (i in options) or (tagged[i]=="NN"):
    		s1.append(i)
    
    for i in range(0,len(s1)):
    	if s1[i] not in words["positive"] and s1[i] not in words["negative"]:
    		ans.append(s1[i])
    		s1.remove(s1[i])
    		if i < len(s1):
    			i+=1
    		else:
    			break
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
    ck = 0
    to_check = ''
    final_ans = []
    temp = []
    
    for i in options:
    	if ' ' in i:
    		to_check = i
    		temp_len = len(to_check.split(' '))
    		for j in to_check.split(' '):
    			if j in ans:
    				ck+=1
    				temp.append(j)
    		if ck > int(temp_len/2)-1 and to_check != '':
    			final_ans.append(to_check)
    			for k in temp:
    				ans.remove(k)
    	ck = 0
    	to_check = ''
    
    
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
    
    final_ans.extend(ans)
    print(final_ans)
