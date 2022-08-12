import add_task as at
import user_interface as ui
import change_deadline as cd
import delete_task as dt
import show_all_tasks as sat

def user_choice():
    chosen_num = ui.menu()
    if chosen_num < 0 or chosen_num > 5:
        print('Ошибка ввода. Число должно соответствовать пунктам меню')
        user_choice()
    elif chosen_num == 0:
        at.create_json()
    elif chosen_num == 1:
        at.add_to_json()
    elif chosen_num == 2:
        cd.change_deadline()
    elif chosen_num == 3:
        dt.delete_task()
    elif chosen_num == 4:
        sat.show_all_tasks()
    elif chosen_num == 5:
        print('Спасибо и до новых встреч!')
        exit() 
