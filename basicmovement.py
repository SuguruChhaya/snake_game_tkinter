from tkinter import *

class Movement():
    def __init__(self):
        self.root = Tk()
        self.my_canvas = Canvas(self.root, height=500, width=500)
        self.my_canvas.grid(row=0, column=0)

        #*I am going to make a grid system by lines
        for height in range(0, 500, 25):
            self.my_canvas.create_line(0, height, 500, height)

        for width in range(0, 500, 25):
            self.my_canvas.create_line(width, 0, width, 500)

        self.item = self.my_canvas.create_rectangle(225, 225, 250, 250, fill='green', tags='item')
        #*Trying to move this thing.
        self.my_canvas.tag_bind('item', '<>')
        

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass



a = Movement()
mainloop()