import csv
n = input()
all_dates=[]
with open ('scientist.txt','r',encoding='utf-8') as file:
        data = file.read().split('\n')[1:-1]
        for i in data:
            s = i.split('#')
            date = s[2]
            all_dates.append(date)
while n!='эксперимент':
    n=n.replace('.','-')
    n=n[-4]+n[-3]+n[-2]+n[-1]+'-'+n[3]+n[4]+'-'+n[0]+n[1]
    with open ('scientist.txt','r',encoding='utf-8') as file:
        data = file.read().split('\n')[1:-1]
        if n not in all_dates:
            print('В этот день ученые отдыхали')
        else:
            for i in data:
                s = i.split('#')
                date = s[2]
                name = s[0].split(' ')
                namenew = name[0]+' '+name[1][0]+'.'+name[2][0]+'.'
                if date==n:
                    print(f'Ученый {namenew} создал препарат: {s[1]} - {date}')
                    break
    n = input()
            
    
