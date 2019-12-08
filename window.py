from tkinter import *
import tkinter.scrolledtext as scroll
from settings import WIDTH


def auth():
    pass


def enter():
    pass

# ######################################## #
# Окно ################################### #
# ######################################## #

root = Tk()
root.geometry('+10+10')
root.title('Вход на GitHub')
root.attributes('-topmost', True)

canvas = Canvas(root, bg='white')
canvas.pack()

# ######################################## #
# Поле авторизации ####################### #
# ######################################## #

lf = LabelFrame(canvas, text='', bd=4, fg='red')
lf.pack()

log = Entry(lf, width=WIDTH, font='Arial 14', fg="light gray")
log.pack()

mail = Entry(lf, width=WIDTH, font='Arial 14', fg="light gray")
mail.pack()

pas = Entry(lf, width=WIDTH, font='Arial 14', fg="light gray")
pas.pack()

rep = Entry(lf, width=WIDTH, font='Arial 14', fg="light gray")
rep.pack()

# ######################################## #
# Подсказки в полях ###################### #
# ######################################## #

log.insert(0, 'Логин')
mail.insert(0, 'E-Mail')
pas.insert(0, 'Пароль')
rep.insert(0, 'Название репозитория')

# ####################################### #
# Кнопка ВХОДА ########################## #
# ####################################### #
btn_login = Button(canvas, text='ВХОД', bg='green', fg='white', command=auth, font='Arial 14 bold')
btn_login.pack()

# ####################################### #
# Терминал ############################## #
# ####################################### #

terminal = LabelFrame(canvas, text=' Терминал ', height=250, bd=4, fg='green')
terminal.pack_propagate(False)
terminal.pack(fill=BOTH)
text = scroll.ScrolledText(terminal, font='Arial 12')
text.pack()

# ####################################### #
# Кнопка ВЫХОДА из программы ############ #
# ####################################### #

btn_exit = Button(canvas, text='ВЫХОД\nиз программы', bg='red', fg='white', command=root.destroy, font='Arial 14 bold')
btn_exit.pack()

root.bind('1', enter)

root.mainloop()