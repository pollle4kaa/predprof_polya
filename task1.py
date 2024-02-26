import csv
sc = [] #все создатели Аллопуринола
all_sc = [] #дубликат таблицы
prep_or=[] #оригинальные препараты
with open ('scientist.txt','r',encoding='utf-8') as file:
    with open ('scientist_origin.txt','w',encoding='utf-8',newline='') as filenew:
        data = file.read().split('\n')[:-1]
        headline = data.pop(0).split('#')
        w = csv.writer(filenew)
        w.writerow(headline)
        for i in data:
            s = i.split('#')
            if s[1]=='Аллопуринол':
                sc.append([s[0],s[2]])
        for i in data:
            s = i.split('#')
            all_sc.append(s)
        all_sc.sort(key = lambda x: x[2])
        for i in range (len(all_sc)):
            scien = all_sc[i][0]
            prep = all_sc[i][1]
            if prep not in prep_or:
                w.writerow(all_sc[i])
                prep_or.append(prep)

sc.sort(key = lambda x: x[1])
print('Разработчиками Аллопуринола были такие люди:')
for i in range (1,len(sc)):
    print(f'{sc[i][0]} - {sc[i][1]}')
print(f'Оригинальный рецепт принадлежит: {sc[0][0]}')
