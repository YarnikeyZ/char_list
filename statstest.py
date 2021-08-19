from tkinter import *
import asyncio

# Окно
window = Tk()
window.title("Stats")
window.geometry('150x550')

# Не обращать внимания на исполнение до последнего!!
# Высчитывает и изменяет переменную бонусных поинтов функ. хар. исходя кол-ва числа поинтов функ. хар.
## Переменная int_points: переменная числа поинтов из функ. хар.
## Переменная bonus_points: переменная печатаемых бонусных поинтов в окне из функ. хар.
async def bonus_calc(int_points, bonus_points):
    if int_points == 1:
        bonus_points.configure(text="[ -5 ]")
    elif 1 < int_points < 4:
        bonus_points.configure(text="[ -4 ]")
    elif 3 < int_points < 6:
        bonus_points.configure(text="[ -3 ]")
    elif 5 < int_points < 8:
        bonus_points.configure(text="[ -2 ]")
    elif 7 < int_points < 10:
        bonus_points.configure(text="[ -1 ]")
    elif 9 < int_points < 12:
        bonus_points.configure(text="[ +0 ]")
    elif 11 < int_points < 14:
        bonus_points.configure(text="[ +1 ]")
    elif 13 < int_points < 16:
        bonus_points.configure(text="[ +2 ]")
    elif 15 < int_points < 18:
        bonus_points.configure(text="[ +3 ]")
    elif 17 < int_points < 20:
        bonus_points.configure(text="[ +4 ]")
    elif 19 < int_points < 22:
        bonus_points.configure(text="[ +5 ]")
    elif 21 < int_points < 24:
        bonus_points.configure(text="[ +6 ]")
    elif 23 < int_points < 26:
        bonus_points.configure(text="[ +7 ]")
    elif 25 < int_points < 28:
        bonus_points.configure(text="[ +8 ]")
    elif 27 < int_points < 30:
        bonus_points.configure(text="[ +9 ]")
    elif int_points == 30:
        bonus_points.configure(text="[ +10 ]")
    else:
        bonus_points.configure(text="!!!err!!!")

# Общие кнопочки
## Переменная action: '+' или '-'
## Переменная int_points: переменная числа поинтов из функ. хар.
## Переменная str_points: переменная печатаемых поинтов в окне из функ. хар.
## Переменная bonus_points: переменная печатаемых бонусных поинтов в окне из функ. хар.
## Функ. bonus_calc высчитывает и изменяет переменную бонусных поинтов функ. хар. исходя кол-ва числа поинтов функ. хар.
async def score_btn(action, int_points, str_points, bonus_points):
    if action == '+':
        if int_points < 30:
            int_points += 1
            str_points.configure(text=int_points)
            await bonus_calc(int_points=int_points, bonus_points=bonus_points)
    elif action == '-':
        if int_points > 1:
            int_points -= 1
            str_points.configure(text=int_points)
            await bonus_calc(int_points=int_points, bonus_points=bonus_points)
    else:
        raise SyntaxError

# Функ. для создания функ. хар.
async def score(row, str_name):
    ## int_points
    int_points=1
    ##  Название
    name = Label(window, text=f' {str_name}', font=("System", 10))
    name.grid(column=1, row=row)
    ## bonus_points
    bonus_points = Label(window, text="[ -5 ]", font=("System", 20))
    bonus_points.grid(column=1, row=row+1)
    ## str_points
    str_points = Label(window, text=int_points, font=("System", 7))
    str_points.grid(column=1, row=row+2)
    ## Кнопачки
    btn_one = Button(window, text="-", command=await score_btn(action='-', int_points=int_points, str_points=str_points, bonus_points=bonus_points), font=("System", 7))
    btn_one.grid(column=0, row=row+2)
    btn_two = Button(window, text="+", command=await score_btn(action='+', int_points=int_points, str_points=str_points, bonus_points=bonus_points), font=("System", 7))
    btn_two.grid(column=2, row=row+2)


async def stats():
    row = 0
    await score(row=row, str_name='Charisma')
    row += 3
    await score(row=row, str_name='Huisma')


loop = asyncio.get_event_loop()
loop.run_until_complete(stats())
window.mainloop()
