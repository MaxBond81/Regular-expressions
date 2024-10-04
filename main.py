from pprint import pprint
import csv
import re

pattern_phone = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_phone = r'+7(\2)\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Приводим в порядок ФИО
contact_list_person = []
for item in contacts_list:
    name = " ".join(item[:3]).split(" ")
    result = [name[0], name[1], name[2], item[3], item[4],re.sub(pattern_phone, sub_phone,item[5]), item[6]]
    contact_list_person.append(result)

# Объединяем информацию в дублях
for person in contact_list_person:
    first_name = person[0]
    last_name = person[1]
    for new_person in contact_list_person:
        new_first_name = new_person[0]
        new_last_name =  new_person[1]
        if first_name == new_first_name and last_name == new_last_name:
            if person[2] == "": person[2] = new_person[2]
            if person[3] == "": person[3] = new_person[3]
            if person[4] == "": person[4] = new_person[4]
            if person[5] == "": person[5] = new_person[5]
            if person[6] == "": person[6] = new_person[6]

# Удяляем дубли
for person in contact_list_person:
    if contact_list_person.count(person) > 1:
        contact_list_person.remove(person)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contact_list_person)