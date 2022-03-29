import pyautogui as p
import time 
p.PAUSE = 2.5

path = 'img\\'

test = path + 'test.png'

delete = path + 'delete.png'
delete_d = path + 'delete_not_active.png'
sort_by_name = path + 'sort_by_name_rb.png'
search_err = path + 'search_err.png'
clear_all = path + 'clear_all.png'
new_date = path + 'new_date.png'
check_date = path + 'check_date.png'
query = path + 'query.png'

def find_btn(btn):
    """Функция поиска кнопки по изображению"""
    btn_position = p.locateOnScreen(btn, confidence = 0.85)
    if btn_position == None:
        btn_position = p.locateOnScreen(btn, confidence = 0.85)
        if btn_position == None:
            print(f'button {btn} not found')
    else:
        p.moveTo(btn_position)
        return btn_position

def delete_one():
    """Функция удаления выбранного исследования"""
    # Нажимаю на кнопку "удалить"
    btn_delete = find_btn(delete)
    p.click(btn_delete)
    # Подтверждаю удаление
    p.press('enter')
   
def delete_many():
    i = 0
    while i <= 48:
        delete_one()
        print(i)
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
        # Опускаюсь ниже и беру в лево
        lm = 60 # left move
        tm = 30 # top move
        p.moveTo(field_name_left+lm, field_name_top+tm)
        # Выбираю исследование
        p.click()

def searching_err():
    """Функция сброса ошибки 'Превышено количество откликов запроса'"""
    # Нажимаю ПКМ в центре ошибки
    err = find_btn(search_err)
    p.click(err, button='right')
    err_left = err[0]
    err_top= err[1]
    # Опускаюсь ниже
    tm = 220
    lm = 200
    p.moveTo(err_left + lm, err_top + tm)
    p.click()

def cleaning():
    """Функция очистки полей"""
    # Нахожу поле с именем
    clear = find_btn(clear_all)
    p.click(clear)
 
def new_date_in():
    """Функция устанавливает дату поиска и заупскает поиск"""
    date = find_btn(new_date)
    p.click(date)
    p.write('12/31/2013')
    check = find_btn(check_date)
    if check is not None:
        p.press('enter')
        p.press('enter')
    else:
        p.press('esc')
        print('Не смог ввести дату')
        time.sleep(436320)

def search_del():
    cleaning()
    new_date_in()
    activation_btn = first_click()
    if activation_btn == False:
        choice_one()
        delete_many()
    else:
        delete_many()
    

def start():
    while True:
        search_del()

start()
