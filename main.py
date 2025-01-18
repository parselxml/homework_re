import csv
import re
from enum import unique
from re import findall

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

new_list = [['last_name', "first_name", "surname", "organization", "position", "phone_number", "mail"]]

pattern_phone_number = r'(\+?[7-8])?\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})'
pattern_ext_number = r'доб.\s?(\d+)'
pattern_mail = r'([\w\.]+@\w+\.+\w+)'

for i in contacts_list[1:]:
    name_data = ','.join(i[:2]).replace(',', ' ').split(' ')
    last_name = name_data[0]
    first_name = name_data[1]
    surname = name_data[2] if len(name_data) > 2 else ''

    organization = i[3]
    position = i[4]


    phone_match = re.search(pattern_phone_number, i[5])
    ext_match = re.search(pattern_ext_number, i[5])
    mail_match = re.search(pattern_mail, i[6])

    phone_number = ''
    mail = ''

    if phone_match:
        phone_number = f'+7({(phone_match.group(2))}){phone_match.group(3)}-{phone_match.group(4)}-{phone_match.group(5)}'

    if ext_match:
        phone_number += f' доб.{ext_match.group(1)}'

    if mail_match:
        mail = mail_match.group(1)

    person_found = False

    for contact in new_list:
        if contact[0] == last_name and contact[1] == first_name:
            if phone_number:
                contact[5] = phone_number
            if mail:
                contact[6] = mail
            person_found = True
            break
    if not person_found:
        new_list.append([last_name, first_name, surname, organization, position, phone_number, mail])




# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_list)
