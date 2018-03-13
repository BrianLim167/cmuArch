# 15-112, Summer 2, Homework 2.2
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

################################################################################
# 1. lookAndSay(a) [20 pts]
def lookAndSay(a):
    ans = []
    count = 0    # stores number of consecutive identical elements
    prev = None  # stores identical element
    ind = -1     # stores current index of ans
    for i in range(len(a)):
        # If the current and previous elements are the same, add to count and
        # update ans.
        if (a[i] == prev):
            count += 1
            ans[ind] = (count,prev)
        # Otherwise, update prev, reset count, go to the next ind of ans, and
        # append a new tuple to ans.
        else:
            prev = a[i]
            count = 1
            ind += 1
            ans.append( (count,prev) )
    return ans
#
################################################################################

################################################################################
# 2. inverseLookAndSay(a) [15 pts]
def inverseLookAndSay(a):
    ans = []
    b = a[:]
    for i in range(len(b)):
        while (b[i][0] > 0): # b[i][0] represents the count of a certain number
            ans.append(b[i][1]) # b[i][1] represents the number that was counted
            b[i] = (b[i][0]- 1 , b[i][1])
    return ans
            
#
################################################################################

################################################################################
# 3. encrypt(plaintext, password) [25 pts]
def encrypt(plaintext, password):
    if ( not (password.isalpha() and password.islower()) ):
        return "password must be all lowercase"
    ans = ""
    # convert plaintext to uppercase and remove non-letters 
    plaintext = onlyAlpha(plaintext.upper())
    password = password.upper()
    for i in range(len(plaintext)):
        # char of password that corresponds to the current char in plaintext
        shiftChar = password[i % len(password)]
        newOrd = ord(plaintext[i]) + (ord(shiftChar) - ord('A'))
        if (newOrd > ord('Z')): # wrap around when newOrd surpasses the alphabet
            newOrd -= 26
        ans += chr(newOrd)
    return ans

def onlyAlpha(s):
    ans = ""
    for i in range(len(s)):
        if (s[i].isalpha()):
            ans += s[i]
    return ans
#
################################################################################

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

def rgbString(red, green, blue): # by Paul Davis
    return "#%02x%02x%02x" % (red, green, blue)

from tkinter import *
 
def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

################################################################################
# 4. runSimpleTortoiseProgram(program, winWidth=500, winHeight=500) [40 pts]
import math

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    displayCode(canvas,program)
    execCode(canvas,program,winWidth,winHeight)
    root.mainloop()

def execCode(canvas,program,winWidth,winHeight):
    color,ang,x,y = "none",0,winWidth/2,winHeight/2
    for line in program.splitlines():
        line = removeComment(line)
        line = line.split() # line is a list of words from one line of code
        if (line == []): continue # ignore lines that only have whitespace
        elif (line[0] == "color"): color = line[1]
        elif (line[0] == "move"):
            if (color != "none"):
                canvas.create_line(x, y,
                                   x + int(line[1])*math.cos(ang), # x+rcos(ang)
                                   y + int(line[1])*math.sin(ang), # y+rsin(ang)
                                   fill=color, width=4)
            x = x + int(line[1])*math.cos(ang)
            y = y + int(line[1])*math.sin(ang)
        elif (line[0] == "left"):
            # subtract argument converted to radians
            ang -= int(line[1])*(math.pi/180)
        elif (line[0] == "right"):
            # add argument converted to radians
            ang += int(line[1])*(math.pi/180)

def removeComment(line):
    for i in range(len(line)):
        if (line[i] == '#'):
            return line[:i]
    return line

def displayCode(canvas,program):
    canvas.create_text(10, 0, text=program,
                       fill="gray", font="Calibri 10",
                       anchor=NW)
#
################################################################################

################################################################################
# Tests
################################################################################

PRINT_TEST = False # determines whether to run the print tests
GRAPHICS_TEST = True # determines whether to run the tk window

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

def testLookAndSayProblems():
    tests = [
        [],
        [1,2,3],
        [1,1,1],
        [-1,2,7],
        [3,3,8,-10,-10,-10],
        [3,3,3,2,2,3,3,1,1,2,2,1,1,1],
        ]
    for test in tests:
        print("lookAndSay("+str(test)+") returns:")
        print(lookAndSay(test))
        sep()
        print("inverseLookAndSay("+str(lookAndSay(test))+") returns:")
        print(inverseLookAndSay(lookAndSay(test)))
        sep()
    sepBig()

def testEncrypt():
    tests = [
        ("",""),
        ("abc",""),
        ("abc","aBC"),
        #("abc","abc%"),
        ("","abc"),
        ("abc","abc"),
        ("Go Team!","azby"),
        ("zzz","bbb"),
        ("zzz zzz z","bbb"),
        ]
    for test in tests:
        print("encrypt"+str(test)+" returns:")
        print(encrypt(test[0],test[1]))
        sep()
    sepBig()

def testRunSimpleTortoiseProgram():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

if (PRINT_TEST):
    testLookAndSayProblems()
    testEncrypt()
if (GRAPHICS_TEST):
    testRunSimpleTortoiseProgram()
