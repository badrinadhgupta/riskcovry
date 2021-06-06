months = ['january', 'february', 'march', 'april', 'may',
          'june', 'july', 'august', 'september',
          'october', 'november', 'december', 'jan',
          'feb', 'mar', 'apr', '', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
def q3(s,options):
    s=s.lower()
    s = s.split(' ')
    am = ''
    dd, dm, dy = 0, 0, 0
    
    for i in range(len(options)):
        options[i]=options[i].lower()
    
    
    for i in s:
        if i in months:
            am = i
        elif len(i)==3:
            if (i[1:3]=='st' or i[1:3]=='nd' or i[1:3]=='rd') and 48<=ord(i[0])<=57:
                dd = int(i[0])
        elif len(i)==2 or len(i)==1:
            try:
                if dy==0:
                    if dd==0:
                        dd = int(i)
                    elif dm ==0:
                        dm = int(i)
                else:
                    if dm==0:
                        dm = int(i)
                    elif dd ==0:
                        dd = int(i)
            except:
                pass
        elif len(i)==4:
            try:
                dy = int(i)
            except:
                if dy == 0:
                    if dd == 0:
                        dd = int(i[0:2])
                    elif dm == 0:
                        dm = int(i[0:2])
                else:
                    if dm == 0:
                        dm = int(i[0:2])
                    elif dd == 0:
                        dd = int(i[0:2])
    
    
    if dm>12 and dd < 13:
        t = dm
        dm = dd
        dd = t
    
    
    if am != '':
        for i in range(len(months)):
            if months[i] == am:
                dm = (i+1) % 12
                break
    t = ''
    if dm<10:
        t = '0'
    
    t1 = ''
    if dd<10:
        t1 = '0'
    
    ans = t1+str(dd)+'/'+t+str(dm)+'/'+str(dy)
    print("Answer :",[ans])
    return [ans]
