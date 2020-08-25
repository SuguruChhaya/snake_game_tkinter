'''
This file is the final file which will contain the starting menus and all.
'''
from tkinter import *
import tkinter.font
import random

class StartWindows():
    player_number = None
    speed_boost = None
    apple_move = None
    loop_apple = None
    can_die_or_no = None
    def __init__(self):
        self.window_1 = Tk()
        StartWindows.player_number = IntVar()
        StartWindows.player_number.set(1)
        one_radiobutton = Radiobutton(self.window_1, text='1 Player', variable=StartWindows.player_number, value=1)
        one_radiobutton.grid(row=0, column=0, sticky=W)
        two_radiobutton = Radiobutton(self.window_1, text='2 Players', variable=StartWindows.player_number, value=2)
        two_radiobutton.grid(row=1, column=0, sticky=W)
        StartWindows.speed_boost = StringVar()
        speed_boost_checkbox = Checkbutton(self.window_1, text='Speed boost enabled', variable=StartWindows.speed_boost, onvalue='On', offvalue='Off')
        speed_boost_checkbox.deselect()
        speed_boost_checkbox.grid(row=2, column=0, sticky=W)
        StartWindows.apple_move = StringVar()
        apple_move_checkbox = Checkbutton(self.window_1, text='Apple moves every 5(?) seconds enabled', variable=StartWindows.apple_move, onvalue='On', offvalue='Off')
        apple_move_checkbox.deselect()
        apple_move_checkbox.grid(row=3, column=0, sticky=W)
        StartWindows.loop_apple = StringVar()
        loop_apple_checkbox = Checkbutton(self.window_1, text='Loop through two apples enabled', variable=StartWindows.loop_apple, onvalue='On', offvalue='Off')
        loop_apple_checkbox.deselect()
        loop_apple_checkbox.grid(row=4, column=0, sticky=W)
        continue_button = Button(self.window_1, text='Continue', command=self.window_2_func)
        continue_button.grid(row=5, column=0)

    def window_2_func(self):
        self.window_1.destroy()
        self.window_2 = Tk()
        player1_control = 'w: up, a: left, s: down, d: right'
        player2_control = 'up arrow: up, left arrow: left, down arrow: down, right arrow: right'

        if StartWindows.player_number.get() == 1:
            if StartWindows.speed_boost.get() == 'On':
                player1_control += ', space bar: speed boost'
            player1_control = Label(self.window_2, text=player1_control)
            player1_control.grid(row=1, column=0)
            StartWindows.can_die_or_no = StringVar()
            can_die = Radiobutton(self.window_2, text='Can Die', variable=StartWindows.can_die_or_no, value='Can Die')
            can_die.grid(row=2, column=0)

        elif StartWindows.player_number.get() == 2:
            if StartWindows.speed_boost.get() == 'On':
                player1_control += ', space bar: speed boost'
                player2_control += ', 0: speed boost'
            player1_control = Label(self.window_2, text=player1_control)
            player1_control.grid(row=1, column=0)
            player2_control = Label(self.window_2, text=player2_control)
            player2_control.grid(row=2, column=0)



        StartWindows.can_die_or_no = StringVar()


            

start = StartWindows()
mainloop()
