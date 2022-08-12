import json
import controller

path_to_db = 'db.json'

def export_txt():
    with open(path_to_db, 'r', encoding = 'UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open ('Export_contacts.txt', 'a', encoding = 'UTF-8') as exported_file:
                exported_file.write('\n' + ' '.join(data[i]['Name'])+ ' ' + ' '.join(
                    data[i]['Surname']) + ' ' + ' '.join(data[i]['Phone number']) + ' ' + ' '.join(data[i]['Comment']))
    print('Контакты успешно экспортированы в файл')
    controller.user_choice()