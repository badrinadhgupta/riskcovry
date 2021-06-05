def q2(s,options):
    s=s.lower()
    #s = s.split(' ')
    #options = ["<5lakh", "5lakh-15lakh", '15lakh-20lakh', '20lakh>']
    for i in range(len(options)):
        options[i]=options[i].lower()
    
    
    req = ''
    for j in s:
       if ord(j) in range(48, 58):
          req += j
            
    if 'lakh' in s:
        req += str(10**5)[1:]
            
    lt, gt = 0, 0
    cur_num = ''
    r1, r2 = '', ''
    d = 0
    ans = ''
    for i in range(len(options)):
       if '<' in options[i]:
          lt = 1
          for j in options[i]:
             if ord(j) in range(48, 58):
                cur_num+= j
       elif '>' in options[i]:
          gt = 1
          for j in options[i]:
             if ord(j) in range(48, 58):
                cur_num+= j
       else:
          for j in options[i]:
             if ord(j) in range(48, 58) and d==0:
                r1+=j
             if j=='-':
                d=1
             if ord(j) in range(48, 58) and d==1:
                r2+=j
       if lt==1:
          if 'lakh' in options[i]:
                cur_num += str(10 ** 5)[1:] 
          if int(req) < int(cur_num):
             ans = options[i]
             break
       if gt==1:
          if 'lakh' in options[i]:
                cur_num += str(10 ** 5)[1:] 
          if int(req) >= int(cur_num):
             ans = options[i]
             break
       if d==1:
          if 'lakh' in options[i]:
                r1 += str(10 ** 5)[1:]
          if 'lakh' in options[i]:
                r2 += str(10 ** 5)[1:]
          if int(r1)<=int(req) and int(r2)>int(req):
             ans = options[i]
    
       lt, gt, d = 0, 0, 0
       r1, r2 = '', ''
       cur_num = ''
    
    return ans
    
