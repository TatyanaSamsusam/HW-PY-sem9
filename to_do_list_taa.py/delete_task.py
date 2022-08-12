import json
import controller

path_to_db = 'to_do.json'

def delete_task():
    name = input('Введите название задачи, которую будем удалять: ')

    with open (path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Task name']:
                del data[i]
    with open (path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('Задача успешно удалена')
    controller.user_choice()
    
