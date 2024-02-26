import csv
all_sc = [] #дубликат таблицы
with open ('scientist.txt','r',encoding='utf-8') as file:
    data = file.read().split('\n')[1:-1]
    for i in data:
        s = i.split('#')
        all_sc.append(s)
    all_sc.sort(key = lambda x: x[2])
    for i in range (5):
        scien = all_sc[i][0]
        prep = all_sc[i][1]
        print(f'{scien}: {prep}')
