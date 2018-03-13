# 15-112, Summer 2, Homework @@@
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################


################################################################################
# ignore_rest
################################################################################

def rgbString(red, green, blue): # by Professor Davis
    return "#%02x%02x%02x" % (red, green, blue)

from tkinter import *
 
def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    root.mainloop()
    print("bye!")

################################################################################
# Tests
################################################################################

printTest = True # determines whether to run the print tests
graphicsTest = False # determines whether to run the tk window

# print separators
def sep():
    if (printTest): print('''
________________________________________________________________________________
''')
def sepBig():
    if (printTest): print('''
################################################################################
################################################################################
################################################################################
''')

if (printTest):
    pass
if (graphicsTest):
    pass
