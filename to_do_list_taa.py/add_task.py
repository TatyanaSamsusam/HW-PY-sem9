import json
import controller

def create_json():
    json_data = []
    with open('to_do.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_choice()

def add_to_json():
    task_name = input('Введите название задачи: ')
    task_details = input('Введите тело задачи: ')
    deadline = input('Введите срок выполнения: ')
    json_data = {
        'Task name': task_name,
        'Task long': task_details,
        'Up to': deadline,
        }
    data = json.load(open('to_do.json'))
    data.append(json_data)
    with open('to_do.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('Новая задача успешно добавлена')
    controller.user_choice()