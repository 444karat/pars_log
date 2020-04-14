import json
import sys
import fileinput

# 1 Получение данных файловой системы
str = input()
str = str.lower()
one = json.loads(str)
ptr = list()
for i in one:
    ptr.append(i.split())
file = dict()
for i in ptr:
    s = set(i[1:])
    file[i[0]] =s
# 2 Получение данных о пользователях
ans = dict()
str = input()
str = str.lower()
one = json.loads(str)
ptr = list()
for i in one:
    ptr.append(i.split())
team = dict()
for i in ptr:
    s = set(i[1:])
    team[i[0]] = s
    ans[i[0]] = 0
# 3 Считывание и обрабтка системного лога
for i in fileinput.input():
    str =i.strip().split()
    if (str[1][0] == "e"):
        ptr = set("x")
    else:
        ptr = set(str[1][0])
    t = team.get(str[0])
    f = file.get(str[2])
    if ptr <= t&f:
        pass
    else:
        ans[str[0]] += 1
# 4 Вывод результатов на экран
ptr = True
print("Отчет о нарушениях:")
for i in ans:
    if ans.get(i) != 0:
        print (i,":",ans.get(i) )
        ptr = False
if (ptr):
    print("Нарушений нет!")
