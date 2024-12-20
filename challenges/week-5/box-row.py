from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    xbox = BOX_SIZE
    ybox = CANVAS_HEIGHT 
    xaxis = 0
    yaxis = CANVAS_HEIGHT - BOX_SIZE
    for i in range(N_BOXES):
        box = canvas.create_rectangle(xaxis, yaxis, xbox, ybox,"white", "black")
        xaxis += BOX_SIZE
        xbox += xbox


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()