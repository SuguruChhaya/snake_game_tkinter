from tkinter import *
import random
import keyboard
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
        self.head_x1 = Snake.my_canvas.coords(self.snake_body[0])[0]
        self.head_y1 = Snake.my_canvas.coords(self.snake_body[0])[1]
        self.head_x2 = Snake.my_canvas.coords(self.snake_body[0])[2]
        self.head_y2 = Snake.my_canvas.coords(self.snake_body[0])[3]

        self.tail_x1 = Snake.my_canvas.coords(self.snake_body[-1])[0]
        self.tail_y1 = Snake.my_canvas.coords(self.snake_body[-1])[1]
        self.tail_x2 = Snake.my_canvas.coords(self.snake_body[-1])[2]
        self.tail_y2 = Snake.my_canvas.coords(self.snake_body[-1])[3]
        # *Since this is the function that will constantly be running, I will want to add my checking functions here.
        # ?So much to debug here
        #*I figured out the reason why the body parts were overlapping.
        #*I have to first check whether the keyboard buttons were pressed/hold first.
        #*I can't just change everything easily
        #!Conveniently, I have the self.snake_direction variable for the last distance chosen.
        
        #*I have to make it so that I can block moves where players try to go in the back direction.
        #?I might want to do something with this is_pressed part.
        #* I will ABSOLUTELY need the part for when the key binding isn't activated
        #!I have to recognize that pressing the keyboard is different from the bind being activated.
        #?I might want to create a new variable which checks whether the KEY BINDING has been activated
        #*I can cancel the variable after moving it.
        if keyboard.is_pressed('w') or keyboard.is_pressed('s') or keyboard.is_pressed('a') or keyboard.is_pressed('d'):
            #*If 
            #!I have a bug in which when I hold the bind button for long and release it, I can go in the opposite way.
            #*To fix this issue, I think I can cancel a specific binding when I press a button.
            #*Like when I press up, I can cancel up and down cuz i won't need it until the next move.
            
            temporary_check = [self.snake_direction, self.last_direction]
            if ('up' in temporary_check and 'down' in temporary_check) or ('left' in temporary_check and 'right' in temporary_check):
                if self.last_direction == 'up':
                    self.up('event')
                elif self.last_direction == 'down':
                    self.down('event')
                elif self.last_direction == 'left':
                    self.left('event')
                elif self.last_direction == 'right':
                    self.right('event')
            
            Snake.my_canvas.move(self.snake_body[-1], self.x, self.y)
        else:
            if self.snake_direction == 'up':
                self.up('event')
            elif self.snake_direction == 'down':
                self.down('event')
            elif self.snake_direction == 'left':
                self.left('event')
            elif self.snake_direction == 'right':
                self.right('event')
            Snake.my_canvas.move(self.snake_body[-1], self.x, self.y)
    
        #Snake.my_canvas.move(self.snake_body[-1], self.x, self.y)
        #!I cannot switch the first and last. Instead I have to insert the last into the front
        self.snake_body.insert(0, self.snake_body[-1])
        del(self.snake_body[-1])

        self.after_var = True

        self.head_x1 = Snake.my_canvas.coords(self.snake_body[0])[0]
        self.head_y1 = Snake.my_canvas.coords(self.snake_body[0])[1]
        self.head_x2 = Snake.my_canvas.coords(self.snake_body[0])[2]
        self.head_y2 = Snake.my_canvas.coords(self.snake_body[0])[3]

        self.tail_x1 = Snake.my_canvas.coords(self.snake_body[-1])[0]
        self.tail_y1 = Snake.my_canvas.coords(self.snake_body[-1])[1]
        self.tail_x2 = Snake.my_canvas.coords(self.snake_body[-1])[2]
        self.tail_y2 = Snake.my_canvas.coords(self.snake_body[-1])[3]

        if Snake.my_canvas.coords(self.snake_body[0]) == Snake.my_canvas.coords(Apple.apple_1):
            self.add_length()
            Snake.my_canvas.delete(Apple.apple_1)
            Apple.apple_count -= 1

        if Apple.apple_count == 0:
            b.create_apple()

        #!Figuring out where the head is.
        #*I think I have to add the head first and then check


        #*The tail coordinates

        #*I will have to change the order of the list too.


        #*Re-initiate the value after list order 


        if self.head_x1 > 350 or self.head_x1 < 0 or self.head_y1 > 350 or self.head_y1 < 0:
            # *If I can go through the walls

            if self.wall_death:
                # *Return to original position
                #*I think I will need a times 2 for the head to pop back
                #?Not necessarily times 2 depending on length
                Snake.my_canvas.move(self.snake_body[0], -self.x, -self.y)
                self.after_var = False
            else:
                # *Could make used moveto()
                #!I need to move the tail instead of the head
                if self.head_x1 > 350:
                    Snake.my_canvas.move(self.snake_body[0], -375, 0)
                elif self.head_x1 < 0:
                    Snake.my_canvas.move(self.snake_body[0], 375, 0)
                elif self.head_y1 > 350:
                    Snake.my_canvas.move(self.snake_body[0], 0, -375)
                elif self.head_y1 < 0:
                    Snake.my_canvas.move(self.snake_body[0], 0, 375)

        self.head_x1 = Snake.my_canvas.coords(self.snake_body[0])[0]
        self.head_y1 = Snake.my_canvas.coords(self.snake_body[0])[1]
        self.head_x2 = Snake.my_canvas.coords(self.snake_body[0])[2]
        self.head_y2 = Snake.my_canvas.coords(self.snake_body[0])[3]

        self.tail_x1 = Snake.my_canvas.coords(self.snake_body[-1])[0]
        self.tail_y1 = Snake.my_canvas.coords(self.snake_body[-1])[1]
        self.tail_x2 = Snake.my_canvas.coords(self.snake_body[-1])[2]
        self.tail_y2 = Snake.my_canvas.coords(self.snake_body[-1])[3]

        if self.after_var:
            self.alive = Snake.my_canvas.after(200, self.movement)
        else:
            Snake.my_canvas.after_cancel(self.alive)

        #*I am saving the last direction so I can block users trying to go the opposite way.
        self.last_direction = self.snake_direction

        print(f'self.x {self.x}')
        print(f'self.y {self.y}')
        print(f'self.snake body: {self.snake_body}')
        print(f'self.head_x1: {self.head_x1}')
        print(f'self.head_y1: {self.head_y1}')
        print(f'self.tail_x1: {self.tail_x1}')
        print(f'self.tail_y1: {self.tail_y1}')

    def add_length(self):
        #*Rather than checking the current distance, I think I should check where the current last object was.
        #*This way, I can add it to the right location even if the snake is doing some crazy twist.
        print('add length')
        # *New rectangles will spawn based on which direction the snake was travelling last

        #*If I am addin to a length larger than 1, the self.snake_x1 must be the coordinates of the last item in the snake body
        #!The following code is unnecessary because the snake body length will always be greater than 1
        '''
        if len(self.snake_body) > 0:
            self.snake_x1 = Snake.my_canvas.coords(self.snake_body[-1])[0]
            self.snake_y1= Snake.my_canvas.coords(self.snake_body[-1])[1]
            self.snake_x2= Snake.my_canvas.coords(self.snake_body[-1])[2]
            self.snake_y2= Snake.my_canvas.coords(self.snake_body[-1])[3]
        '''
        if self.snake_direction == 'up':
            self.add_length_x1 = self.tail_x1
            # *Careful with the coordinate system
            self.add_length_y1 = self.tail_y1 + 25
            self.add_length_x2 = self.tail_x2
            self.add_length_y2 = self.tail_y2 + 25

        elif self.snake_direction == 'down':
            self.add_length_x1 = self.tail_x1
            self.add_length_y1 = self.tail_y1 - 25
            self.add_length_x2 = self.tail_x2
            self.add_length_y2 = self.tail_y2 - 25

        elif self.snake_direction == 'left':
            self.add_length_x1 = self.tail_x1 + 25
            self.add_length_y1 = self.tail_y1
            self.add_length_x2 = self.tail_x2 + 25
            self.add_length_y2 = self.tail_y2

        elif self.snake_direction == 'right':
            self.add_length_x1 = self.tail_x1 - 25
            self.add_length_y1 = self.tail_y1
            self.add_length_x2 = self.tail_x2 - 25
            self.add_length_y2 = self.tail_y2

      # *As long as the rectange is in the list, I don't think I have to name it.
        self.snake_body.append(Snake.my_canvas.create_rectangle(
            self.add_length_x1, self.add_length_y1, self.add_length_x2, self.add_length_y2, fill='green'))

    #*When the snake gets longer and starts twisting, this will not be enough
    def up(self, event):
        #*I think print cannot print inside a binded function
        self.x = self.head_x1 - self.tail_x1
        self.y = self.head_y1 - self.tail_y1 - 25
        self.snake_direction = 'up'
        self.up_bind = self.root.bind("<w>", lambda event: self.up(event))
        self.down_bind = self.root.bind("<s>", lambda event: self.down(event))
        self.left_bind = self.root.bind("<a>", lambda event: self.left(event))
        self.right_bind = self.root.bind(
            "<d>", lambda event: self.right(event))
        self.root.unbind('<w>', self.up_bind)
        if len(self.snake_body) > 1:
            self.root.unbind('<s>',self.down_bind)

    def down(self, event):
        self.x = self.head_x1 - self.tail_x1
        self.y = self.head_y1 - self.tail_y1 + 25
        self.snake_direction = 'down'
        self.up_bind = self.root.bind("<w>", lambda event: self.up(event))
        self.down_bind = self.root.bind("<s>", lambda event: self.down(event))
        self.left_bind = self.root.bind("<a>", lambda event: self.left(event))
        self.right_bind = self.root.bind(
            "<d>", lambda event: self.right(event))
        self.root.unbind('<s>', self.down_bind)
        if len(self.snake_body) > 1:
            self.root.unbind('<w>', self.up_bind)

    def left(self, event):
        #!The reason it overlaps when I don't press anything is because the self.x and self.y values aren't changed.
        #* This is because I didn't constantly hold the keybindings.
        #*There is a weird bug which causes the ting to skip numbers. I should fix that.
        self.x = self.head_x1 - self.tail_x1 -25
        self.y = self.head_y1 - self.tail_y1
        self.snake_direction = 'left'
        self.up_bind = self.root.bind("<w>", lambda event: self.up(event))
        self.down_bind = self.root.bind("<s>", lambda event: self.down(event))
        self.left_bind = self.root.bind("<a>", lambda event: self.left(event))
        self.right_bind = self.root.bind(
            "<d>", lambda event: self.right(event))
        self.root.unbind('<a>', self.left_bind)
        if len(self.snake_body) > 1:
            self.root.unbind('<d>', self.right_bind)

    def right(self, event):
        self.x = self.head_x1 - self.tail_x1 + 25
        self.y = self.head_y1 - self.tail_y1
        self.snake_direction = 'right'
        #*Re-bind and unbind
        self.up_bind = self.root.bind("<w>", lambda event: self.up(event))
        self.down_bind = self.root.bind("<s>", lambda event: self.down(event))
        self.left_bind = self.root.bind("<a>", lambda event: self.left(event))
        self.right_bind = self.root.bind(
            "<d>", lambda event: self.right(event))
        self.root.unbind('<d>', self.right_bind)
        if len(self.snake_body) > 1:
            self.root.unbind('<a>', self.left_bind)


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
