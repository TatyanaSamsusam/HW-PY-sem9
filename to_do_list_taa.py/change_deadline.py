import json
import controller

path_to_db = 'to_do.json'
def change_deadline():
    name = input('Введите название задачи, срок которой будем менять: ')
    with open (path_to_db, 'r', encoding='UTF8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Task name']:
                data[i]['Up to'] = input('Новый cрок выполнения: ')
    with open (path_to_db, 'w', encoding='UTF8') as file:
        json.dump(data, file, indent=4)
    print('Срок выполнения задачи успешно изменен')
    controller.user_choice()

