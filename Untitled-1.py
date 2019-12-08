from tkinter import *

root = Tk()
root.geometry('+10+10')
root.title('Вход на GitHub')
root.attributes('-topmost', True)

canvas = Canvas(root, bg='white')
canvas.pack()

root.mainloop()