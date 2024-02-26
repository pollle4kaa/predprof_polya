import csv
from random import choice
alp='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789' #алфавит
with open ('scientist.txt','r',encoding='utf-8') as file:
    with open ('scientist_password.csv','w',encoding='utf-8',newline='') as filenew:
        data = file.read().split('\n')[:-1]
        headline = data.pop(0).split('#')
        headline.append('login')
        headline.append('password')
        w = csv.writer(filenew)
        w.writerow(headline)
        for i in data:
            s = i.split('#')
            name = s[0].split(' ')
            login = name[0]+'_'+name[1][0]+name[2][0]
            password=''
            while (len([x for x in password if x in 'qwertyuiopasdfghjklzxcvbnm'])>0 and len([x for x in password if x in 'QWERTYUIOPASDFGHJKLZXCVBNM'])>0 and len([x for x in password if x in '0123456789'])>0)==0:
                password=choice(alp)+choice(alp)+choice(alp)+choice(alp)+choice(alp)+choice(alp)+choice(alp)+choice(alp)+choice(alp)+choice(alp) #генерация пароля длиной 10 символов
            s.append(login)
            s.append(password)
            w.writerow(s)
        
            

