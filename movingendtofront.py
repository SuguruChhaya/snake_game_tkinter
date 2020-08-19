from tkinter import *
import random

'''
In this version, i am going to use the strategy of moving the end block to the front instead of moving everything.
I am going to use tags to check which is the head.
'''

class Snake():

    def __init__(self):
        self.root = Tk()
        Snake.my_canvas = Canvas(self.root, height=375, width=375, bg='black')
        Snake.my_canvas.grid(row=0, column=0)

        # *I am going to make a grid system by lines
        # *15 by 15 grid
        for height in range(0, 375, 25):
            Snake.my_canvas.create_line(0, height, 500, height, fill='white')

        for width in range(0, 375, 25):
            Snake.my_canvas.create_line(width, 0, width, 500, fill='white')

        self.snake_body = []
        self.snake_body.append(Snake.my_canvas.create_rectangle(225, 225, 250, 250, fill='light green', tags='head'))
        # *Trying to move this thing.
        # https://stackoverflow.com/questions/15269682/python-tkinter-canvas-fail-to-bind-keyboard
        self.up_bind = self.root.bind("<w>", lambda event: self.up(event))
        self.down_bind = self.root.bind("<s>", lambda event: self.down(event))
        self.left_bind = self.root.bind("<a>", lambda event: self.left(event))
        self.right_bind = self.root.bind(
            "<d>", lambda event: self.right(event))
        # *Default movement is up
        self.x = 0
        self.y = -25
        self.snake_direction = 'up'
        self.last_direction = 'up'
        # *I am going to store the turns in the form of a nested list.
        # *The first four floats will be the coordinates where I have to turn.
        # *The fifth string will be the direction I need to turn to.
        self.turns = []
        # *Just a variable to allow wall passing or no.
        self.wall_death = False

    # A great reference for controlling the speed of the moving boxes.

    def movement(self):
        print(self.x)
        print(self.y)
        # *Since this is the function that will constantly be running, I will want to add my checking functions here.
        # ?So much to debug here

        Snake.my_canvas.move(self.snake_body[-1], self.x, self.y)

        self.after_var = True
        #!Figuring out where the head is.
        self.head = self.snake_body[0]
        self.snake_x1 = Snake.my_canvas.coords(self.head)[0]
        self.snake_y1 = Snake.my_canvas.coords(self.head)[1]
        self.snake_x2 = Snake.my_canvas.coords(self.head)[2]
        self.snake_y2 = Snake.my_canvas.coords(self.head)[3]

        #*The tail coordinates
        self.tail_x1 = Snake.my_canvas.coords(self.snake_body)[0]
        self.tail_y1 = Snake.my_canvas.coords(self.snake_body)[1]
        self.tail_x2 = Snake.my_canvas.coords(self.snake_body)[2]
        self.tail_y2 = Snake.my_canvas.coords(self.snake_body)[3]

        #*I will have to cvhange the order of the list too.
        self.head_index = self.snake_body.index(self.head)
        self.snake_body[self.head_index], self.snake_body[-1] = self.snake_body[-1], self.head
        print(self.snake_body)

        if Snake.my_canvas.coords(self.head) == Snake.my_canvas.coords(Apple.apple_1):
            self.add_length()
            Snake.my_canvas.delete(Apple.apple_1)
            Apple.apple_count -= 1

        if Apple.apple_count == 0:
            b.create_apple()

        if self.snake_x1 > 350 or self.snake_x1 < 0 or self.snake_y1 > 350 or self.snake_y1 < 0:
            # *If I can go through the walls
            if self.wall_death:
                # *Return to original position
                Snake.my_canvas.move(self.head, -self.x, -self.y)
                self.after_var = False
            else:
                # *Could make used moveto()
                if self.snake_x1 > 350:
                    Snake.my_canvas.move(self.head, -375, 0)
                elif self.snake_x1 < 0:
                    Snake.my_canvas.move(self.head, 375, 0)
                elif self.snake_y1 > 350:
                    Snake.my_canvas.move(self.head, 0, -375)
                elif self.snake_y1 < 0:
                    Snake.my_canvas.move(self.head, 0, 375)
    

        if self.after_var:
            self.alive = Snake.my_canvas.after(200, self.movement)
        else:
            Snake.my_canvas.after_cancel(self.alive)

    def add_length(self):
        # *New rectangles will spawn based on which direction the snake was travelling last

        #*If I am addin to a length larger than 1, the self.snake_x1 must be the coordinates of the last item in the snake body
        if len(self.snake_body) > 0:
            self.snake_x1 = Snake.my_canvas.coords(self.snake_body[-1])[0]
            self.snake_y1= Snake.my_canvas.coords(self.snake_body[-1])[1]
            self.snake_x2= Snake.my_canvas.coords(self.snake_body[-1])[2]
            self.snake_y2= Snake.my_canvas.coords(self.snake_body[-1])[3]
        if self.snake_direction == 'up':
            self.add_length_x1 = self.snake_x1
            # *Careful with the coordinate system
            self.add_length_y1 = self.snake_y1 + 25
            self.add_length_x2 = self.snake_x2
            self.add_length_y2 = self.snake_y2 + 25

        elif self.snake_direction == 'down':
            self.add_length_x1 = self.snake_x1
            self.add_length_y1 = self.snake_y1 + 25
            self.add_length_x2 = self.snake_x2
            self.add_length_y2 = self.snake_y2 + 25

        elif self.snake_direction == 'left':
            self.add_length_x1 = self.snake_x1 + 25
            self.add_length_y1 = self.snake_y1
            self.add_length_x2 = self.snake_x2 + 25
            self.add_length_y2 = self.snake_y2

        elif self.snake_direction == 'right':
            self.add_length_x1 = self.snake_x1 - 25
            self.add_length_y1 = self.snake_y1
            self.add_length_x2 = self.snake_x2 - 25
            self.add_length_y2 = self.snake_y2

      # *As long as the rectange is in the list, I don't think I have to name it.
        self.snake_body.append(Snake.my_canvas.create_rectangle(
            self.add_length_x1, self.add_length_y1, self.add_length_x2, self.add_length_y2, fill='green'))

    #*When the snake gets longer and starts twisting, this will not be enough
    def up(self, event):
        self.x = self.snake_x1 - self.
        self.y = -25 * len(self.snake_body)
        self.snake_direction = 'up'

    def down(self, event):
        self.x = 0
        self.y = 25 * len(self.snake_body)
        self.snake_direction = 'down'

    def left(self, event):
        #*There is a weird bug which causes the ting to skip numbers. I should fix that.
        self.x = -25 * len(self.snake_body)
        self.y = 0
        self.snake_direction = 'left'

    def right(self, event):
        self.x = 25 * len(self.snake_body)
        self.y = 0
        self.snake_direction = 'right'


class Apple():
    apple_count = 0

    def __init__(self):
        # *Creating the list in which the apple can spawn.
        self.apple_coord_list = []
        # *The list of which the apple can land
        for i in range(0, 375, 25):
            self.apple_coord_list.append(i)

        self.apple_x_list = self.apple_coord_list.copy()
        self.apple_y_list = self.apple_coord_list.copy()

    def create_apple(self):
        self.apple_x1 = random.choice(self.apple_x_list)
        self.apple_x2 = self.apple_x1 + 25
        self.apple_y1 = random.choice(self.apple_y_list)
        self.apple_y2 = self.apple_y1 + 25
        Apple.apple_1 = Snake.my_canvas.create_rectangle(
            self.apple_x1, self.apple_y1, self.apple_x2, self.apple_y2, fill='red')
        Apple.apple_count += 1


a = Snake()
b = Apple()
b.create_apple()
a.movement()
mainloop()
