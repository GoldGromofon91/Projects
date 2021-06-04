import csv
from collections import defaultdict, OrderedDict
"""
    Формат файла: login tuid docid jud cjud.
    Оценки могут принимать значение [0, 1], т.е. задание, которое сделали асессоры, имеет бинарную шкалу.
    Используя данные об оценках, установите, какие асессоры хуже всего справились с заданием. 
    На какие показатели вы ориентировались и какие метрики вы использовали для ответа на этот вопрос? 
    Можно ли предложить какие-то новые метрики для подсчета качества асессоров с учетом природы оценок у этого бинарного задания?
    
    login — логин асессора; uid — id асессора (user id); 
    docid — id оцениваемого документа (document id); jud — оценка асессора (judgement); 
    cjud — правильная оценка (correct judgement); разделитель — табуляция \t.
"""
user_s = defaultdict(lambda : 0)
with open("data_task3.csv") as file:
    next(file) 
    data = csv.reader(file, delimiter= '\t')
    
    for login, uid, docid, jud, cjud in data:
        if jud == cjud: 
            user_s[uid] = user_s[uid] + 1
        continue


sorted_dct = OrderedDict(sorted(user_s.items(), key = lambda el:el[1]))
print(sorted_dct)

"""
data_set = defaultdict(list)
top_user = defaultdict(list)
res = defaultdict(list)
with open("data_task3.csv") as file:
    next(file) 
    data = csv.reader(file, delimiter= '\t')
    
    for login, uid, docid, jud, cjud in data:
        data_set[int(docid)].append((int(uid), int(jud), int(cjud)))


for key in data_set:
    for obj_in in range(len(data_set[key])):
        total_point = 0
        if data_set[key][obj_in][1] == data_set[key][obj_in][2]:
            total_point += 1
            top_user[data_set[key][obj_in][0]].append(total_point)
        else:
            top_user[data_set[key][obj_in][0]].append(total_point)
            continue

for key in top_user:
    res[key].append(sum(top_user[key]))


print(res[192])
"""