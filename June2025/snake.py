from tkinter import *
import random


GAME_WIDTH = 650
GAME_HEIGHT = 650
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake():
    pass

class Food():
    pass

def next_turn():
    pass

def check_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake game")
window.resizable(False,False)

score = 0
direct = 'down'

label = Label(window,text='Score:{}'.format(score),font=('consolas',40))
label.pack()

canvas = Canvas(window, background=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
window.mainloop()