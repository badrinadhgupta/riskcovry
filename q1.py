import nltk
def q1(s, options):
    #s=s.lower()
    o = options[:]
    tokens = nltk.word_tokenize(s)
    tagged = nltk.pos_tag(tokens)
    tagged=dict(tagged)
    
    for i in range(len(options)):
        options[i]=options[i].lower()
    s=s.lower()
    words={"positive":["have","suffer","got","diagnose"],"negative":["no","not","don't","do not"]}
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
    	ans.append("others")
    if "none" in options and len(ans)==0:
    	ans.append("none")
    
    final_ans.extend(ans)
    f = []
    for i in final_ans:
        for j in range(0,len(options)):
            if(options[j] == i):
                f.append(o[j])
                break
    print("Answer :",f)
    return f
