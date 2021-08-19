from tkinter import *

# Окно
window = Tk()
window.title('Stats')
window.geometry('150x550')

# Не обращать внимания на исполнение до последнего!!
# Высчитывает и изменяет переменную бонусных поинтов функ. хар. исходя кол-ва числа поинтов функ. хар.
## Переменная int_points: переменная числа поинтов из функ. хар.
## Переменная bonus_points: переменная печатаемых бонусных поинтов в окне из функ. хар.
def bonus_calc(int_points):
    if int_points == 1:
        new_bonus_points = '[ -5 ]'
    elif 1 < int_points < 4:
        new_bonus_points = '[ -4 ]'
    elif 3 < int_points < 6:
        new_bonus_points = '[ -3 ]'
    elif 5 < int_points < 8:
        new_bonus_points = '[ -2 ]'
    elif 7 < int_points < 10:
        new_bonus_points = '[ -1 ]'
    elif 9 < int_points < 12:
        new_bonus_points = '[ +0 ]'
    elif 11 < int_points < 14:
        new_bonus_points = '[ +1 ]'
    elif 13 < int_points < 16:
        new_bonus_points = '[ +2 ]'
    elif 15 < int_points < 18:
        new_bonus_points = '[ +3 ]'
    elif 17 < int_points < 20:
        new_bonus_points = '[ +4 ]'
    elif 19 < int_points < 22:
        new_bonus_points = '[ +5 ]'
    elif 21 < int_points < 24:
        new_bonus_points = '[ +6 ]'
    elif 23 < int_points < 26:
        new_bonus_points = '[ +7 ]'
    elif 25 < int_points < 28:
        new_bonus_points = '[ +8 ]'
    elif 27 < int_points < 30:
        new_bonus_points = '[ +9 ]'
    elif int_points == 30:
        new_bonus_points = '[ +10 ]'
    else:
        new_bonus_points = '!!!err!!!'
    return new_bonus_points

# Общие кнопочки
## Переменная action: '+' или '-'
## Переменная int_points: переменная числа поинтов из функ. хар.
## Переменная str_points: переменная печатаемых поинтов в окне из функ. хар.
## Переменная bonus_points: переменная печатаемых бонусных поинтов в окне из функ. хар.
## Функ. bonus_calc высчитывает и изменяет переменную бонусных поинтов функ. хар. исходя кол-ва числа поинтов функ. хар.
def score_btn(action, int_points, str_points, bonus_points):
    if action == '-':
        if int_points > 1:
            int_points -= 1
            str_points.configure(text=int_points)
            bonus_points.configure(text=bonus_calc(int_points=int_points))
    elif action == '+':
        if int_points < 30:
            int_points += 1
            str_points.configure(text=int_points)
            bonus_points.configure(text=bonus_calc(int_points=int_points))
    else:
        raise SyntaxError

# Функ. для создания функ. хар.
def score(row, str_name):
    ## int_points
    int_points=1
    ##  Название
    name = Label(window, text=f' {str_name}', font=('System', 10))
    name.grid(column=1, row=row)
    ## bonus_points
    bonus_points = Label(window, text='[ -5 ]', font=('System', 20))
    bonus_points.grid(column=1, row=row+1)
    ## str_points
    str_points = Label(window, text=int_points, font=('System', 7))
    str_points.grid(column=1, row=row+2)
    ## Кнопачки
    btn_one = Button(window, text='-', command=score_btn(action='-', int_points=int_points, str_points=str_points, bonus_points=bonus_points), font=('System', 7))
    btn_one.grid(column=0, row=row+2)
    btn_two = Button(window, text='+', command=score_btn(action='+', int_points=int_points, str_points=str_points, bonus_points=bonus_points), font=('System', 7))
    btn_two.grid(column=2, row=row+2)

def stats(names):
    row = 0
    for str_name in names:
        score(row=row, str_name=str_name)
        row += 3

stats(['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'])
window.mainloop()
