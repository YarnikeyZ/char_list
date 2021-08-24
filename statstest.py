from tkinter import *

# Окно
window = Tk()
window.title('Stats')
window.geometry('150x550')

def bonus_calc(int_points):
    new_bonus_points = "[ {:+} ]".format(int_points // 2 - 5)
    return new_bonus_points

def score(column, row, str_name):
    int_points = 1
    ##  Название
    name = Label(window, text=f' {str_name}', font=('System', 10))
    name.grid(column=column+1, row=row)
    ## bonus_points
    bonus_points = Label(window, text='[ -5 ]', font=('System', 20))
    bonus_points.grid(column=column+1, row=row+1)
    ## str_points
    str_points = Label(window, text=int_points, font=('System', 7))
    str_points.grid(column=column+1, row=row+2)
    ## Кнопки
    def score_btn(action):
        nonlocal int_points
        if action == '+':
            if int_points < 30:
                int_points += 1
        elif action == '-':
            if int_points > 1:
                int_points -= 1
        else:
            raise SyntaxError
        str_points.configure(text=int_points)
        bonus_points.configure(text=bonus_calc(int_points=int_points))
    
    minus = lambda: score_btn(action='-')
    plus = lambda: score_btn(action='+')
    btn_one = Button(window, text='-', command=minus, font=('System', 7))
    btn_two = Button(window, text='+', command=plus, font=('System', 7))
    btn_one.grid(column=column, row=row+2)
    btn_two.grid(column=column+2, row=row+2)

def stats(column, row, names):
    for str_name in names:
        score(column=column, row=row, str_name=str_name)
        row += 3

stats(0, 0, ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'])
window.mainloop()
