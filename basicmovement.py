from tkinter import *
import random
class Snake():
    
    def __init__(self):
        self.root = Tk()
        Snake.my_canvas = Canvas(self.root, height=375, width=375, bg='black')
        Snake.my_canvas.grid(row=0, column=0)

        #*I am going to make a grid system by lines
        #*15 by 15 grid
        for height in range(0, 375, 25):
            Snake.my_canvas.create_line(0, height, 500, height, fill='white')

        for width in range(0, 375, 25):
            Snake.my_canvas.create_line(width, 0, width, 500, fill='white')

        self.item = Snake.my_canvas.create_rectangle(225, 225, 250, 250, fill='green', tags='item')
        #*Trying to move this thing.
        #https://stackoverflow.com/questions/15269682/python-tkinter-canvas-fail-to-bind-keyboard
        self.up_bind = self.root.bind("<w>", lambda event: self.up(event))
        self.down_bind = self.root.bind("<s>", lambda event: self.down(event))
        self.left_bind = self.root.bind("<a>", lambda event: self.left(event))
        self.right_bind = self.root.bind("<d>", lambda event: self.right(event))
        #*Default movement is up
        self.x = 0
        self.y = -25
        #*Just a variable to allow wall passing or no.
        self.wall_death = True

    #A great reference for controlling the speed of the moving boxes.

    def movement(self):
        #*Since this is the function that will constantly be running, I will want to add my checking functions here.
        Snake.my_canvas.move(self.item, self.x, self.y)

        print(Snake.my_canvas.coords(self.item))
        print(Snake.my_canvas.coords(Apple.apple_1))

        #*I should definitely make a variable to manage whether the after function will run next time or not.
        self.after_var = True
        if Snake.my_canvas.coords(self.item) == Snake.my_canvas.coords(Apple.apple_1):
            Snake.my_canvas.after_cancel(self.alive)
            print('equal')
        
        #*If hit the wall, freeze.
        self.snake_x1 = Snake.my_canvas.coords(self.item)[0]
        self.snake_y1 = Snake.my_canvas.coords(self.item)[1]
        self.snake_x2 = Snake.my_canvas.coords(self.item)[2]
        self.snake_y2 = Snake.my_canvas.coords(self.item)[3] 

        if self.snake_x1 > 350 or self.snake_x1 < 0 or self.snake_y1 > 350 or self.snake_y1 < 0:
            #*If I can go through the walls
            if self.wall_death:
                #*Return to original position
                Snake.my_canvas.move(self.item, -self.x, -self.y)
                Snake.my_canvas.after_cancel(self.alive)
            else:
                if self.snake_x1 > 350:
                    Snake.my_canvas.move(self.item, -375, 0)
                elif self.snake_x1 < 0:
                    Snake.my_canvas.move(self.item, 375, 0)
                elif self.snake_y1 > 350:
                    Snake.my_canvas.move(self.item, 0, -375)
                elif self.snake_y1 < 0:
                    Snake.my_canvas.move(self.item, 0, 375)
                self.alive = self.my_canvas.after(200, self.movement)
            

        else:
            self.alive = Snake.my_canvas.after(200, self.movement)





    def up(self, event):
        self.x = 0
        self.y = -25


    def down(self, event):
        self.x = 0
        self.y = 25


    def left(self, event):
        self.x = -25
        self.y = 0


    def right(self, event):
        self.x = 25
        self.y = 0

class Apple():
    apple_count = 0

    def __init__(self):
        #*Creating the list in which the apple can spawn.
        self.apple_coord_list = []
        #*The list of which the apple can land
        for i in range(0, 375, 25):
            self.apple_coord_list.append(i)
        
        self.apple_x_list = self.apple_coord_list.copy()
        self.apple_y_list = self.apple_coord_list.copy()

        self.apple_x1 = random.choice(self.apple_x_list)
        self.apple_x2 = self.apple_x1 + 25
        self.apple_y1 = random.choice(self.apple_y_list)
        self.apple_y2 = self.apple_y1 + 25
        Apple.apple_1 = Snake.my_canvas.create_rectangle(self.apple_x1, self.apple_y1, self.apple_x2, self.apple_y2, fill='red')






a = Snake()
b = Apple()
a.movement()
mainloop()