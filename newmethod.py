from tkinter import *
import random


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

        self.head = Snake.my_canvas.create_rectangle(
            225, 225, 250, 250, fill='light green', tags='item')
        self.snake_body = []
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
        # *Since this is the function that will constantly be running, I will want to add my checking functions here.
        # ?So much to debug here
        if self.snake_direction == self.last_direction:
            # *I will first check whether there are any items in the self.turns list I have to catch up on.
            if len(self.turns) == 0:
                print(self.snake_body)
                Snake.my_canvas.move(self.head, self.x, self.y)
                for item in self.snake_body:
                    Snake.my_canvas.move(item, self.x, self.y)
            # *I have an issue in which the snake head moves two
            # *The case in which the head has turned, but the body hasn't kept up.
            else:
                print(self.turns)
                # *I think I have to keep the head and all the already turned body parts separate in a list.
                # *These parts have to be treated separately.
                Snake.my_canvas.move(self.head, self.x, self.y)
                self.not_moved = self.snake_body.copy()
                for part in self.snake_body:
                    for i in range(len(self.turns)):
                        if part in self.turns[i][2]:
                            if self.turns[i][1] == 'up':
                                Snake.my_canvas.move(part, 0, -25)
                            elif self.turns[i][1] == 'down':
                                Snake.my_canvas.move(part, 0, 25)
                            elif self.turns[i][1] == 'left':
                                Snake.my_canvas.move(part, -25, 0)
                            elif self.turns[i][1] == 'right':
                                Snake.my_canvas.move(part, 25, 0)
                            # *The rest of the snake which doesn't turn yet
                            if Snake.my_canvas.coords(part) == self.turns[i][0]:
                                print(part)
                                print(self.turns[i][2])
                                self.turns[i][2].remove(part)

                            if len(self.turns[i][2]) == 0:
                                self.turns = self.turns[1:]
                        self.not_moved.remove(part)
                        break

                for part in self.not_moved:
                    if self.snake_direction == 'up':
                        Snake.my_canvas.move(part, 0, -25)
                    elif self.snake_direction == 'down':
                        Snake.my_canvas.move(part, 0, 25)
                    elif self.snake_direction == 'left':
                        Snake.my_canvas.move(part, -25, 0)
                    elif self.snake_direction == 'right':
                        Snake.my_canvas.move(part, 25, 0)

        else:
            # *I will obviously have to get the coords of the head and check add the turning point
            # *Temporary variable to store list
            turn_add = []
            turn_add.append(Snake.my_canvas.coords(self.head))
            turn_add.append(self.last_direction)
            #?I think since the snake body changes, the thing mutates in the whole nested list
            #*Using a tuple solved the issue of it mutating
            #!But since a tuple cannot remove objects, I need to find a different solution
            self.snake_body_copy = self.snake_body.copy()
            turn_add.append(self.snake_body_copy)
            #?Due to the value corresponding to snake_body being changed, the snake_body itself changes too.
            #*To prevent this, I should make a copy of the snake variable
            #!I will have keep track of which body parts have already catched up and which didn't.
            self.turns.append(turn_add)
            print(self.turns)
            Snake.my_canvas.move(self.head, self.x, self.y)
            if len(self.snake_body_copy) == 0:
                self.turns = self.turns[1:]
            self.not_moved = self.snake_body.copy()
            for part in self.snake_body:
                for i in range(len(self.turns)):
                    if part in self.turns[i][2]:
                        if self.turns[i][1] == 'up':
                            Snake.my_canvas.move(part, 0, -25)
                        elif self.turns[i][1] == 'down':
                            Snake.my_canvas.move(part, 0, 25)
                        elif self.turns[i][1] == 'left':
                            Snake.my_canvas.move(part, -25, 0)
                        elif self.turns[i][1] == 'right':
                            Snake.my_canvas.move(part, 25, 0)
                    # *The rest of the snake which doesn't turn yet
                    if Snake.my_canvas.coords(part) == self.turns[i][0]:
                        self.turns[i][2].remove(part)
                        if len(self.turns[i][2]) == 0:
                            self.turns = self.turns[1:]
                    self.not_moved.remove(part)
                    break
            # *I have to keep it outside of the for-loop so that it applies when the snake body length is 0

            for part in self.not_moved:
                if self.snake_direction == 'up':
                    Snake.my_canvas.move(part, 0, -25)
                elif self.snake_direction == 'down':
                    Snake.my_canvas.move(part, 0, 25)
                elif self.snake_direction == 'left':
                    Snake.my_canvas.move(part, -25, 0)
                elif self.snake_direction == 'right':
                    Snake.my_canvas.move(part, 25, 0)

        self.snake_x1 = Snake.my_canvas.coords(self.head)[0]
        self.snake_y1 = Snake.my_canvas.coords(self.head)[1]
        self.snake_x2 = Snake.my_canvas.coords(self.head)[2]
        self.snake_y2 = Snake.my_canvas.coords(self.head)[3]

        # *I should definitely make a variable to manage whether the after function will run next time or not.
        self.after_var = True
        if Snake.my_canvas.coords(self.head) == Snake.my_canvas.coords(Apple.apple_1):
            self.add_length()
            Snake.my_canvas.delete(Apple.apple_1)
            Apple.apple_count -= 1
            self.after_var = True
        if Apple.apple_count == 0:
            b.create_apple()

        # *Check if there are constantly 1 or more apples


        # *If hit the wall, freeze.



        if self.after_var:
            self.alive = Snake.my_canvas.after(1000, self.movement)
        else:
            Snake.my_canvas.after_cancel(self.alive)

        # *Storing direction to see if there was a turn
        self.last_direction = self.snake_direction

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

    def up(self, event):
        self.x = 0
        self.y = -25
        self.snake_direction = 'up'

    def down(self, event):
        self.x = 0
        self.y = 25
        self.snake_direction = 'down'

    def left(self, event):
        self.x = -25
        self.y = 0
        self.snake_direction = 'left'

    def right(self, event):
        self.x = 25
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
