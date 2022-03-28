import pyautogui as p
import time

path = 'img\\'

test = path + 'test.png'

delete = path + 'delete.png'
delete_d = path + 'delete_not_active.png'
delete_yes = path + 'delete_yes.png'
sort_by_name = path + 'sort_by_name_rb.png'

def find_btn(btn):
    """Функция поиска кнопки по изображению"""
    btn_position = p.locateOnScreen(btn, confidence = 0.7)
    if btn_position == None:
        print(f'button {btn} not found')
        btn_position = False
        return 
    else:
        p.moveTo(btn_position)
        time.sleep(3)
        return btn_position

def delete_one():
    """Функция удаления выбранного исследования"""
    # Нажимаю на кнопку "удалить"
    btn_delete = find_btn(delete)
    p.click()
    time.sleep(5)
    # Подтверждаю удаление
    btn_yes = find_btn(delete_yes)
    if btn_yes == False:
        btn_yes = find_btn(delete_yes)
    p.click()
    time.sleep(5)
    
def delete_many():
    i = 0
    while i <= 48:
        delete_one()
        i = i + 1

def first_click():
    """Функция определения определения доступности кнопки 'Удалить'"""
    btn_active = find_btn(delete_d)
    if btn_active == None:
        return True
    else:
        return False

def choice_one():
    """Функиция выбора исследования"""
    # Нажимаю ПКМ на поле 'Имя пациента'
    field_name = find_btn(sort_by_name)
    if field_name == None:
        print('field "Имя пациента" not found')
    else:
        field_name_left = field_name[0]
        field_name_top = field_name[1]
        p.click(field_name, button='right')
        # Опускаюсь ниже
        lm = 60 # left move
        tm = 30 # top move
        p.moveTo(field_name_left+lm, field_name_top+tm)
        # Выбираю исследование
        p.click()

def start():
    activation_btn = first_click()
    if activation_btn == False:
        choice_one()
        delete_many()
    else:
        delete_many()
    
start()