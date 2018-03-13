# 15-112, Summer 2, Homework 4.2
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

from tkinter import *
import random

# Initialize the data which will be used to draw on the screen.
def init(data):
    # load data as appropriate
    data.rows = 15
    data.cols = 10
    data.margin = 20
    initBoard(data)
    initTetrisPieces(data)
    newFallingPiece(data)
    data.isGameOver = False
    data.score = 0

def initBoard(data):
    data.board = []
    for row in range(data.rows):
        data.board.append([])
        for col in range(data.cols):
            data.board[row].append("blue")

def initTetrisPieces(data):
    #Seven "standard" pieces (tetrominoes)
    iPiece = [[ True,  True,  True,  True ]]

    jPiece = [[ True, False, False ],
              [ True, True,  True ]]

    lPiece = [[ False, False, True ],
              [ True,  True,  True ]]

    oPiece = [[ True, True],
              [ True, True]]

    sPiece = [[ False, True, True ],
              [ True,  True, False ]]

    tPiece = [[ False, True, False ],
              [ True,  True, True ]]

    zPiece = [[ True,  True, False ],
              [ False, True, True ]]
    data.tetrisPieces =       [iPiece,jPiece,lPiece,oPiece,sPiece,tPiece,zPiece]
    data.tetrisPieceColors =  ["red","yellow","magenta","pink","cyan","green","orange"]

# These are the CONTROLLERs.
# IMPORTANT: CONTROLLER does *not* draw at all!
# It only modifies data according to the events.
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if (data.isGameOver):
        if (event.keysym == 'r'): init(data)
        return
    if (event.keysym == "Up"): rotateFallingPiece(data,False)
    elif (event.keysym == "Down"): moveFallingPiece(data,1,0)
    elif (event.keysym == "Left"): moveFallingPiece(data,0,-1)
    elif (event.keysym == "Right"): moveFallingPiece(data,0,1)

def timerFired(data):
    if (data.isGameOver): return
    if (not moveFallingPiece(data,1,0)):
        placePiece(data)
        newFallingPiece(data)
        removeFullRows(data)
        if (not fallingPieceIsLegal(data)): data.isGameOver = True

# remove filled rows and push other rows to the bottom
def removeFullRows(data):
    newRow = data.rows-1
    fullRows = 0
    for oldRow in range(data.rows-1,-1,-1):
        if (isFull(data.board[oldRow])):
            fullRows += 1
        else:
            for col in range(data.cols):
                data.board[newRow][col] = data.board[oldRow][col]
            newRow -= 1
    for row in range(newRow+1):
        for col in range(data.cols):
            data.board[row][col] = "blue"
    data.score += fullRows ** 2

def isFull(row):
    for col in range(len(row)):
        if (row[col] == "blue"):
            return False
    return True

# spawn a piece at the top of the board
def newFallingPiece(data):
    pieceInd = random.randint(0,len(data.tetrisPieces)-1)
    data.piece = data.tetrisPieces[pieceInd]
    data.pieceColor = data.tetrisPieceColors[pieceInd]
    data.pieceRow = 0
    data.pieceCol = data.cols//2 - len(data.piece[0])//2
    
def moveFallingPiece(data, drow, dcol):
    data.pieceRow += drow
    data.pieceCol += dcol
    if (not fallingPieceIsLegal(data)):
        data.pieceRow -= drow
        data.pieceCol -= dcol
        return False
    return True

def rotateFallingPiece(data,isClockwise):
    oldData = (data.piece,data.pieceRow,data.pieceCol)
    if (isClockwise): pass # not yet implemented
    else:
        newPiece = []
        for newRow in range(len(data.piece[0])-1,-1,-1):
            newPiece.append([])
            for newCol in range(len(data.piece)):
                newPiece[-1].append(data.piece[newCol][newRow])
    newPieceRow = data.pieceRow + len(data.piece)//2 - len(newPiece)//2
    newPieceCol = data.pieceCol + len(data.piece[0])//2 - len(newPiece[0])//2
    data.piece = newPiece
    data.pieceRow = newPieceRow
    data.pieceCol = newPieceCol
    if (not fallingPieceIsLegal(data)):
        (data.piece,data.pieceRow,data.pieceCol) = oldData

def fallingPieceIsLegal(data):
    for row in range(len(data.piece)):
        bRow = row + data.pieceRow
        if (not 0 <= bRow < data.rows): return False
        for col in range(len(data.piece[0])):
            bCol = col + data.pieceCol
            if ( data.piece[row][col] and
                 not (0 <= bCol < data.cols and
                      data.board[bRow][bCol] == "blue") ): return False
    return True

# edit board when the piece lands
def placePiece(data):
    for row in range(len(data.piece)):
        for col in range(len(data.piece[0])):
            if (data.piece[row][col]):
                data.board[data.pieceRow+row][data.pieceCol+col] = data.pieceColor

# This is the VIEW
# IMPORTANT: VIEW does *not* modify data at all!
# It only draws on the canvas.
def redrawAll(canvas, data):
    # draw in canvas
    if (data.isGameOver):
        drawOver(canvas, data)
        return
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    drawScore(canvas, data)

def drawOver(canvas, data):
    canvas.create_text(data.width//2,data.height//2-50,
                       text="Score: %d" % data.score,font="Arial 30")
    canvas.create_text(data.width//2,data.height//2,
                       text="You Lose!",font="Arial 40")
    canvas.create_text(data.width//2,data.height//2+50,
                       text="Hit 'r' to continue",font="Arial 25")

def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas, data, row, col, data.board[row][col])

def drawCell(canvas, data, row, col, color):
    width = (data.width - 2 * data.margin) / data.cols
    height =  (data.height - 2 * data.margin) / data.rows
    canvas.create_rectangle(data.margin + col*width,
                            data.margin + row*height,
                            data.margin + (col+1)*width,
                            data.margin + (row+1)*height,
                            fill=color)

def drawFallingPiece(canvas, data):
    for row in range(len(data.piece)):
        for col in range(len(data.piece[0])):
            if (data.piece[row][col]):
                drawCell(canvas, data,
                         data.pieceRow + row, data.pieceCol + col,
                         data.pieceColor)

def drawScore(canvas, data):
    canvas.create_text(data.width//2,data.height,anchor=S,
                       text="Score: %d" % data.score,font="Arial 12")
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
    data.timerDelay = 800 # milliseconds
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

run(440, 640)
