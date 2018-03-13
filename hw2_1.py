# 15-112, Summer 2, Homework 2.1
######################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
######################################

######################################################################
# Place your non-graphics solutions here!
######################################################################

######################################################################
## 1. patternedMessage(message, pattern) [30 pts]
import string # for string.whitespace
def patternedMessage(message, pattern):
    ans = ""
    for i in range(len(string.whitespace)):
        #removes all whitespace in message
        message = message.replace(string.whitespace[i],"")
    pattern = pattern.strip('\n') #removes trailing and leading newlines
    char = 0 # tracks which char from message will be used next
    for i in range(len(pattern)):
        if (pattern[i] in string.whitespace):
            ans += pattern[i]
        else:
            ans += message[char % len(message)]
            char += 1
    return ans
######################################################################

######################################################################
## 2. topLevelFunctionNames(code) [35 pts]
def topLevelFunctionNames(code):
    code = '\n' + code
    commented,tripleQuoted,tripleDoubleQuoted = False,False,False
    quoted,doubleQuoted,ans = False,False,""
    while len(code) > 0:
        if (code[0] == '#'):                             # #
            code = removeComment(code)
            
        elif (len(code) >= 3 and code[0:3] == "\'\'\'"): # '''
            code = removeTripleQuote(code)
            
        elif (len(code) >= 3 and code[0:3] == "\"\"\""): # """
            code = removeTripleDoubleQuote(code)
            
        elif (code[0] == '\''):                          # '
            code = removeQuote(code)
            
        elif (code[0] == '\"'):                          # "
            code = removeDoubleQuote(code)
            
        elif (len(code) >= 6 and code[0:5] == "\ndef "):
            if (not functionName(code) in ans.split('.')):
                ans += '.' + functionName(code) # add function name to ans
            code = code[5:]
        else: code = code[1:]
    return ans.replace('.',"",1)

def removeComment(code):
    i = 1
    while (i < len(code) and code[i] != '\n'):
        i += 1
    return code[i:]
def removeTripleQuote(code):
    i = 3
    while (i < len(code) - 3 and code[i:i+3] != "\'\'\'"):
        i += 1
    return code[i+3:]
def removeTripleDoubleQuote(code):
    i = 3
    while (i < len(code) - 3 and code[i:i+3] != "\"\"\""):
        i += 1
    return code[i+3:]
def removeQuote(code):
    i = 1
    while (code[i] != '\''):
        i += 1
    return code[i+1:]
def removeDoubleQuote(code):
    i = 3
    while (code[i] != '\"'):
        i += 1
    return code[i+1:]
def functionName(code):
    i = 5
    while (code[i] != '('):
        i += 1
    return code[5:i]
######################################################################

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your graphics solutions here!
######################################################################

def rgbString(red, green, blue): # by Paul Davis
    return "#%02x%02x%02x" % (red, green, blue)

######################################################################
## 3. drawGradient(canvas, x0, y0, x1, y1) [15 pts]
def drawGradient(canvas, x0, y0, x1, y1):
    width = x1 - x0
    for i in range(10,0,-1):
        color = int(25.5*i)
        canvas.create_rectangle(x0,y0,
                                x0 + width*0.1*i,y1,
                                fill=rgbString(color,color,color),
                                width=0)
######################################################################

######################################################################
## 4. drawGrid(canvas, x0, y0, x1, y1) [20 pts] 
def drawGrid(canvas, x0, y0, x1, y1):
    width = x1 - x0
    height = y1 - y0
    num = 1
    for col in range(4):
        for row in range(8):
            color = (row + col + 1) % 2 * 255
            canvas.create_rectangle(x0 + width*col/4,y1 - height*row/8,
                                    x0 + width*(col+1)/4,y1 - height*(row+1)/8,
                                    fill=rgbString(color,color,color))
            canvas.create_text(x0 + width*(col+.5)/4,y1 - height*(row+.5)/8,
                               text = str(num),
                               fill="red")
            num += 1
######################################################################

######################################################################
## 5. bonus(canvas, x0, y0, x1, y1) [2 pts] 
def bonus(canvas, x0, y0, x1, y1):
    width = x1 - x0
    height = y1 - y0
    num = 2
    for row in range(6):
        for col in range(7):
            if (num <= 31):
                month = " July "
            else:
                month = " Aug "
            canvas.create_rectangle(x0 + width*col/7, y0 + height*row/6,
                                    x0 + width*(col+1)/7, y0 + height*(row+1)/6,
                                    fill=rectRgb(row,col))
            canvas.create_text(x0 + width*col/7, y0 + height*row/6,
                               text=month + str(num % 31),
                               anchor=NW)
            canvas.create_text(x0 + width*(col+.5)/7, y0 + height*(row+.5)/6,
                               text=note(row,col))
            num += 1

def rectRgb(row,col):
    if (col == 0 or col == 6):
        return rgbString(150,150,150)
    elif ( (row == 1 and col == 1) or (1 <= row <= 4 and col == 5) ):
        return rgbString(80,170,80)
    elif (row == 0 and col == 2):
        return rgbString(220,200,70)
    elif ( (row == 3 and col == 1) or (row == 5 and col == 5) ):
        return rgbString(50,150,200)
    elif (row == 5 and col == 3):
        return rgbString(240,190,190)
    return rgbString(255,255,255)
def note(row,col):
    if (row == 0 and col == 2):
        return "Holiday"
    elif (row == 1 and col == 1):
        return "Quiz 1"
    elif (row == 1 and col == 5):
        return "Quiz 2"
    elif (row == 2 and col == 5):
        return "Quiz 3"
    elif (row == 3 and col == 1):
        return "Exam 1"
    elif (row == 3 and col == 5):
        return "Quiz 4"
    elif (row == 4 and col == 5):
        return "Quiz 5"
    elif (row == 5 and col == 3):
        return "TP Due"
    elif (row == 5 and col == 5):
        return "Exam 2"
    return ""
######################################################################
    
######################################################################
# Drivers: do NOT modify this code
######################################################################
from tkinter import *

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,
        fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):
        canvas.create_rectangle(170, 50, 570, 450, width=4)
        drawFn(canvas, 170, 50, 570, 450)
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, 
            fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = [drawGradient, drawGrid, bonus]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in range(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, 
            command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

PRINT_TEST = False # determines whether to print information for test purposes
GRAPHICS_TEST = True # determines whether to open the tk window

# print separators
def sep():
    print('''
________________________________________________________________________________
''')
def sepBig():
    print('''
################################################################################
################################################################################
################################################################################
''')

# Test functions

def testPatternedMessage():
    alphabet = "  ABCDEF   GHIJKLM   NOPQR  STUV WXYZ"
    
    print(patternedMessage("Go Pirates!!!", """
***************
******   ******
***************
"""))
    sep()
    print(patternedMessage("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""))
    sep()
    print(patternedMessage("Go Steelers!",
"""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
"""))
    print(patternedMessage(alphabet,''' p p pp
ppp ppppp pppppppp
ppppppppppppp
'''))
    sep()
    print(patternedMessage(alphabet,''' ooooooo oo
ooo oooooooooo oooooooo oooooo
o oooooooo oooooo oooooo o        ooooooo  o'''))
    sepBig()

def testTopLevelFunctionNames():
    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    print(topLevelFunctionNames(code))
    sep()
    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    print(topLevelFunctionNames(code))
    sep()
    code = '''\
"""
#def fq()
"""
def a()
def b()
def c()
def a()
'''
    print(topLevelFunctionNames(code))
    sep()
    code = '''\
#"""
def a()
'''
    print(topLevelFunctionNames(code))
    sep()
    code = '''
#def fq()
def abc(): "def bcd()"
'''
    print(topLevelFunctionNames(code))
    sep()
    code = '''
defx()
defdef y()
def a(): def z()
'''
    print(topLevelFunctionNames(code))
    sepBig()

def main():
    # include function calls for your own test functions
    if (PRINT_TEST):
        testPatternedMessage()
        testTopLevelFunctionNames()
    if (GRAPHICS_TEST):
        graphicsMain()
    

if __name__ == "__main__":
     main()

