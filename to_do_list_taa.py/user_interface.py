import int_check

def start():
    greeting = 'Привет, я cписок дел. Выбери, что хочешь сделать: '
    print(greeting)

def menu():
    create_task_list = '0. Создать новый список дел'
    create_new_task = '1. Создать новую задачу'
    change_task = '2. Редактировать срок выполнения задачи'
    delete_task = '3. Удалить задачу'
    show_all_tasks = '4. Показать все задачи'
    exit = '5. Выйти из программы'
    print(f'{create_task_list}\n{create_new_task}\n{change_task}\n{delete_task}\n{show_all_tasks}\n{exit}')
    return int_check.int_check()
