# 15-112, Summer 2, Homework 4.2
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

from tkinter import *
import random

# MODEL VIEW CONTROLLER (MVC)
####################################
# MODEL:       the data
# VIEW:        redrawAll and its helper functions
# CONTROLLER:  event-handling functions and their helper functions
####################################


####################################
# customize these functions
####################################


# Initialize the data which will be used to draw on the screen.
def init(data):
    # load data as appropriate
    data.rows = 8
    data.cols = 15
    data.headRow = data.rows//2
    data.headCol = data.cols//2
    initBoard(data)
    data.dir = (1,0)
    placeFood(data)
    data.isGameOver = False
    data.margin = 5
    data.isIgnoreStep = False
    data.isPaused = False
    data.score = 0
    data.highscores = []
    data.scoreGap = 60
    data.timerDelay = 400
    data.walls = dict()
        
def placeFood(data):
    r = random.randint(0, data.rows-1)
    c = random.randint(0, data.cols-1)
    while (data.board[r][c] != 0):
        r = random.randint(0, data.rows-1)
        c = random.randint(0, data.cols-1)
    data.board[r][c] = -1

def placePoison(data):
    r = random.randint(0, data.rows-1)
    c = random.randint(0, data.cols-1)
    while (data.board[r][c] != 0 or
           (r == data.headRow + data.dir[0] and c == data.head + data.dir[1])):
        r = random.randint(0, data.rows-1)
        c = random.randint(0, data.cols-1)
    data.board[r][c] = -2

def initBoard(data):
    data.board = []
    for row in range(data.rows):
        data.board.append([0] * data.cols)
    data.board[data.headRow][data.headCol] = 1


# These are the CONTROLLERs.
# IMPORTANT: CONTROLLER does *not* draw at all!
# It only modifies data according to the events.
def mousePressed(event, data):
    # use event.x and event.y
    if (data.isPaused and not data.isGameOver):
        w = data.width - 2 * data.margin
        h = data.height - 2 * data.margin
        r = int(event.y // (h / data.rows))
        c = int(event.x // (w / data.cols))
        if (data.board[r][c] == 0):
            data.board[r][c] = -3
            data.walls[(r,c)] = 0
        elif (data.board[r][c] == -3):
            data.board[r][c] = 0
            del data.walls[(r,c)]
        
    
def keyPressed(event, data):
    # use event.char and event.keysym
    if (event.char == "r"):
        temp = data.highscores
        init(data)
        data.highscores = temp
        return
    if (event.char == 'p'):
        data.isPaused = not data.isPaused
        return
    if (data.isPaused or data.isGameOver): return
    if (event.keysym == 'Up'): data.dir = (-1, 0)
    elif (event.keysym == 'Down'): data.dir = (1, 0)
    elif (event.keysym == 'Left'): data.dir = (0, -1)
    elif (event.keysym == 'Right'): data.dir = (0, 1)
    takeStep(data)
    data.isIgnoreStep = True

def timerFired(data):
    if (data.isPaused or data.isGameOver): return
    elif (data.isIgnoreStep):
        data.isIgnoreStep = False
    else:
        takeStep(data)
    
def takeStep(data):
    drow, dcol = data.dir
    newHeadRow = data.headRow + drow
    newHeadCol = data.headCol + dcol
    
    # snake moves off board or hits self or hits poison
    if (newHeadRow < 0 or newHeadRow >= data.rows or 
        newHeadCol < 0 or newHeadCol >= data.cols or 
        data.board[newHeadRow][newHeadCol] > 0 or
        data.board[newHeadRow][newHeadCol] == -2):
        gameOver(data)
        return

    elif (data.board[newHeadRow][newHeadCol] == -1 ):
        # hit food
        data.board[newHeadRow][newHeadCol] = \
            data.board[data.headRow][data.headCol] + 1
        
        data.headRow = newHeadRow
        data.headCol = newHeadCol
        placeFood(data)
        data.score += 1
        if (data.score == 3):
            data.timerDelay = 200
            placePoison(data)
    elif (data.board[newHeadRow][newHeadCol] == 0 or
          data.board[newHeadRow][newHeadCol] == -3):
        # move snake forward
        if (data.board[newHeadRow][newHeadCol] == -3):
            if (data.score == 0): gameOver(data)
            else: data.score -= 1
        data.board[newHeadRow][newHeadCol] = \
            data.board[data.headRow][data.headCol] + 1
        
        data.headRow = newHeadRow
        data.headCol = newHeadCol
        removeTail(data)
    for wall in data.walls:
        data.walls[wall] += 1

def gameOver(data):
    data.isGameOver = True
    for wall in data.walls:
        if (data.walls[wall] >= 20): data.score += 1
    data.highscores.append(data.score)
    data.highscores = sorted(data.highscores)
    if (len(data.highscores) > 3): data.highscores.pop(0)

def removeTail(data):
    for row in range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] > 0:
                data.board[row][col] -= 1

# This is the VIEW
# IMPORTANT: VIEW does *not* modify data at all!
# It only draws on the canvas.
def redrawAll(canvas, data):
    # draw in canvas
    if (data.isGameOver):
        drawGameOver(canvas, data)
        return
    drawBoard(canvas, data)
    canvas.create_text(data.width//2,10,anchor=N,
                       text=data.score,font="Arial 18",fill="deep pink")

def drawGameOver(canvas, data):
    for i in range(len(data.highscores)):
            canvas.create_text(data.width//2,data.height//2-i*data.scoreGap,
                               text=data.highscores[i],font="Arial 50")

def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawSnakeCell(canvas, data, row, col)
        
def drawSnakeCell(canvas, data, row, col):
    margin = data.margin
    w = data.width - 2 * margin
    h = data.height - 2 * margin
    cellW = w / data.cols
    cellH = h / data.rows
    x0 = cellW * col
    y0 = cellH * row
    x1 = cellW * (col + 1)
    y1 = cellH * (row + 1)
    fill = "white"
    if (data.isPaused): fill = "gray"
    if (data.board[row][col] > 0):
        fill= "black"
    elif (data.board[row][col] == -1):
        fill = "green"
        if (data.isPaused): fill = "dark green"
    elif (data.board[row][col] == -2):
        fill = "red"
        if (data.isPaused): fill = "dark red"
    elif (data.board[row][col] == -3):
        fill = "brown"
        if (data.isPaused): fill = "firebrick"
    canvas.create_rectangle(x0+margin,y0+margin,x1+margin,y1+margin, fill=fill)



####################################
####################################
# use the run function as-is
####################################
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 400 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1500, 800)
