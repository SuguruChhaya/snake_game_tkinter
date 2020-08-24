from tkinter import *
root = Tk()


def a(event):
    global a_bind
    print('a')
    root.unbind('<w>', a_bind)

a_bind = root.bind('<w>', lambda event: a(event))

mainloop()