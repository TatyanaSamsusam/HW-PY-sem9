
def int_check():
    try: 
        any_number = int(input('Введите число: '))
        return any_number
    except ValueError:
        print('Это должно быть целое число')
        return int_check()
