from graphics import Canvas
import random
import time

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    #row for loop that iterates x input from total bricks in base.
    for row in range(BRICKS_IN_BASE):
        numbricks = BRICKS_IN_BASE - row #bricks in row calculation
        #xy start position and x's /2 will centralise x axis
        x_start = (CANVAS_WIDTH - numbricks * BRICK_WIDTH) / 2
        y_start = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT

        #create brick -> col * BRICK_WIDTH will move to right of current brick
        for col in range(numbricks):
            lb(canvas, x_start + col * BRICK_WIDTH, y_start)

#Brick laying function, takes in start xy and has it own end for xy
def lb(canvas, left_x, top_y):
    right_x = left_x + BRICK_WIDTH
    bot_y = top_y + BRICK_HEIGHT
    canvas.create_rectangle(left_x, top_y, right_x, bot_y, 'black')
    canvas.create_rectangle(left_x + 1, top_y + 1, right_x - 1, bot_y - 1, 'brown')
    time.sleep(0.02)

if __name__ == '__main__':
    main()