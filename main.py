#lastname,firstname,surname,organization,position,phone,email
aa = "lastname,firstname,surname,organization,position,phone," \
     "email Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с " \
     "федеральными органами власти Управления налогообложения имущества и доходов физических лиц," \
     "+7 (495) 913-04-78,opendata@nalog.ru " \
     "Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037," \
     "Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168," \
     "Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,," \
     "Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru" \
     "Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru" \
     "Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792)," \
     "Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru"
#поиск номеров 1 ---- "(8|\+7)?\s*\((\d+)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)"gm   +7(\2)\3-\4-\5
#поиск номеров 2 ---- "(8|\+7)[-\s](\d+)[-\s](\d+)[-\s](\d{2})(\d{2})"gm
#поиск номеров 3 ---- "(8|\+7)(\d{3})(\d{3})(\d{2})(\d+)"gm
#поиск доп номеров ---- "доб. \d+"gm


from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
#Регулярка для отлова телефона и доп телефона
patern = r'(8|\+7)?[\s-]?[-\s(]?(\d{3})[-\s)]?[-\s)]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?[(]?(доб.)?\s?(\d{4})?'
#for i in contacts_list:
  #for ii in i:
  #  resalt = re.sub(patern, r'+7(\2)\3-\4-\5', ii)
  #print(i)

#['lastname','firstname','surname','organization','position','phone','email']
new_book = []
new = ''
for i in contacts_list:
  a1, a2, a3, a4, a5 = i[0].split(), i[1].split(), i[2].split(), i[3], i[4]
  fio = a1 + a2 + a3
  print(fio)

  #print(new_book)




# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)