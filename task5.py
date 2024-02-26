import csv
from random import choice
def hash(n):
    '''
    Функция создает хэш для каждой строки таблицы
    
    Описание аргументов:
    n - служит для вызова функции, является любым значением

    примечание - код не работает моментально из-за объемной перестановки с помощью модуля random (choice)
    примерное время работы кода - 17 секунд
    '''
    answer=0 
    s=[] #массив, который позже будет заполнен числами от 0 до 1023 для дальнейшей работы
    for i in range (1024):
        s.append(i)
    ans=[] #массив - таблица перестановок чисел от 0 до 1023
    while len(ans)!=len(s):
        a = choice(s)
        if a not in ans:
            ans.append(a)
    for i in ans:
        i=str(i)
        count=0
        for j in i:
            count+=ord(j)
        indexx = count%1024
        indexx = ans.index(indexx)
        answer+=indexx
    return answer%2048
with open ('scientist.txt','r',encoding='utf-8') as file:
    with open ('scientist _with_hash.csv','w',encoding='utf-8',newline='') as filenew:
        data = file.read().split('\n')[:-1]
        headline = data.pop(0).split('#')
        h = ['hash'] #добавление столбца с названием hash
        h.append(headline[0])
        h.append(headline[1])
        h.append(headline[2])
        h.append(headline[3])
        w = csv.writer(filenew)
        w.writerow(h)
        for i in data:
            s = i.split('#')
            newline = [hash(i)]
            newline.append(s[0])
            newline.append(s[1])
            newline.append(s[2])
            newline.append(s[3])
            w.writerow(newline)
        
            

