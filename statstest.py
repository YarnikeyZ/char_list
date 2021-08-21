from tkinter import *

# Окно
window = Tk()
window.title('Stats')
window.geometry('150x550')

# Высчитывает и возвращает переменную новых бонусных поинтов исходя числа поинтов функ. хар.
## Переменная int_points: переменная числа поинтов из функ. хар.
## Переменная new_bonus_points: переменная возвращаемых бонусных поинтов
def bonus_calc(int_points):
    points_calc ={
        1:'[ -5 ]', 2:'[ -4 ]', 3:'[ -4 ]', 4:'[ -3 ]', 5:'[ -3 ]', 6:'[ -2 ]', 7:'[ -2 ]', 8:'[ -1 ]', 9:'[ -1 ]', 10:'[ +0 ]',
        11:'[ +0 ]', 12:'[ +1 ]', 13:'[ +1 ]', 14:'[ +2 ]', 15:'[ +2 ]', 16:'[ +3 ]', 17:'[ +3 ]', 18:'[ +4 ]', 19:'[ +4 ]', 20:'[ +5 ]',
        21:'[ +5 ]', 22:'[ +6 ]', 23:'[ +6 ]', 24:'[ +7 ]', 25:'[ +7 ]', 26:'[ +8 ]', 27:'[ +8 ]', 28:'[ +9 ]', 29:'[ +9 ]', 30:'[ +10 ]'
    }
    new_bonus_points = points_calc[int_points]
    return new_bonus_points

# Общие кнопочки
## Переменная action: '+' или '-'
## Переменная int_points: переменная числа поинтов из функ. хар.
## Переменная str_points: переменная печатаемых поинтов в окне из функ. хар.
## Переменная bonus_points: переменная печатаемых бонусных поинтов в окне из функ. хар.
## Функ. bonus_calc высчитывает и возвращает переменную новых бонусных поинтов исходя числа поинтов функ. хар.
def score_btn(action, int_points, str_points, bonus_points):
    if action == '-':
        if int_points > 1:
            int_points -= 1
    elif action == '+':
        if int_points < 30:
            int_points += 1
    else:
        raise SyntaxError
    str_points.configure(text=int_points)
    bonus_points.configure(text=bonus_calc(int_points=int_points))

# Функ. для создания функ. хар.
def score(column, row, str_name):
    int_points=1
    ##  Название
    name = Label(window, text=f' {str_name}', font=('System', 10))
    name.grid(column=column+1, row=row)
    ## bonus_points
    bonus_points = Label(window, text='[ -5 ]', font=('System', 20))
    bonus_points.grid(column=column+1, row=row+1)
    ## str_points
    str_points = Label(window, text=int_points, font=('System', 7))
    str_points.grid(column=column+1, row=row+2)
    ## Кнопачки
    minus = lambda: score_btn(action='-', int_points=int_points, str_points=str_points, bonus_points=bonus_points)
    plus = lambda: score_btn(action='+', int_points=int_points, str_points=str_points, bonus_points=bonus_points)
    btn_one = Button(window, text='-', command=minus,font=('System', 7))
    btn_two = Button(window, text='+', command=plus,font=('System', 7))
    btn_one.grid(column=column, row=row+2)
    btn_two.grid(column=column+2, row=row+2)

def stats(column, row, names):
    for str_name in names:
        score(column=column, row=row, str_name=str_name)
        row += 3

stats(0, 0, names = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'])
window.mainloop()
