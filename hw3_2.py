# 15-112, Summer 2, Homework 3.2
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################


################################################################################
# ignore_rest
################################################################################

################################################################################
# 1. The Memory game [100 pts]                                                 #
import random,time

# useful constants for various functions
def constants(function):
    if (function == "display"):
        NUM_OF_NEWLINES = 80
        STANDARD_CARD_SIZE = -4
        return (NUM_OF_NEWLINES,STANDARD_CARD_SIZE)
    if (function == "userInput"):
        POINTS_PER_PAIR = 5
        return POINTS_PER_PAIR

def playMemoryGame(rows=3,cols=3,seed=None):
    try:
        timeStart,solved,score = time.time(),False,0
        # 2d lists of the board values and of the visibility of the board values
        valGrid,visGrid = [],[]
        # randomized 1d list of values that will be used to build valGrid
        valList = generateValues(rows*cols,seed)
        
        for row in range(rows):
            # initialize the row
            valGrid.append([])
            visGrid.append([])
            for col in range(cols):
                value = valList.pop()
                valGrid[row].append(value)
                # blanks are considered to be visible
                if (value == 0): visGrid[row].append(True)
                # everything else is initially invisible
                else: visGrid[row].append(False)
        
        display(valGrid,visGrid,score)
        # continue to ask for input until the game is finished
        while (not solved): (solved,score) = userInput(valGrid,visGrid,score)
        #show the total time that the program ran when the game is finished
        print("TIME : %d seconds" % int(time.time() - timeStart))
        
    except KeyboardInterrupt: pass # CTRL-C exits the game
    # if the user gives invalid arguments, print info about how to use the
    # program
    except: info() 

# randomized 1d list of values that will be used to build valGrid
def generateValues(n,seed):
    valList = []
    if (n % 2 == 1): # odd n generates a single blank,represented as 0
        valList.append(0)
        n -= 1
    for i in range(n):
        valList.append(i//2 + 1) # append 2 of each number from 1 to n//2
    random.seed(seed)
    random.shuffle(valList) # randomize the order of the values
    return valList

# print the board
def display(valGrid,visGrid,score):
    (NUM_OF_NEWLINES,STANDARD_CARD_SIZE) = constants("display")
    ans = "\n" * NUM_OF_NEWLINES
    ans += "Done playing? Hit 'CTRL-C' to exit the game.\n"
    ans += "Confused? Enter '?' for info.\n"
    ans += "   "
    for col in range(len(valGrid[0])):
        ans += "   " + chr(col + ord('A')) # alphabetic labels
    ans += "\n   #"
    for col in range(len(valGrid[0])):
        ans += "####"
    for row in range(len(valGrid)):
        ans += '\n'
        ans += (" "+str(row + 1))[-2:] + " #" # numeric labels
        for col in range(len(valGrid[row])):
            if (valGrid[row][col] == 0): ans += "    " # 0 represents a blank
            elif (visGrid[row][col]):
                ans += ("   "+str(valGrid[row][col]))[STANDARD_CARD_SIZE:]
            else: ans += " [ ]" # [ ] represents a hidden card
    ans += "\nSCORE: %d points" % score
    print(ans)

# asks for input from the user and modifies/displays the board accordingly
def userInput(valGrid,visGrid,score):
    userInput,POINTS_PER_PAIR = "",constants("userInput")
    # user should input a first card
    while (not isValidInput(userInput,len(valGrid),len(valGrid[0]))):
        userInput = input("Choose a card to uncover: ").upper()
    # rowOne and colOne are the coordinates of the first card
    rowOne,colOne = int(userInput[1:]) - 1 , ord(userInput[0]) - ord('A')
    # if the first card is already visible, the user made a mistake; make the
    # user try again
    if (visGrid[rowOne][colOne]): return (inputError(),score)
    # set the first card to be visible; reset userInput
    visGrid[rowOne][colOne],userInput = True,""
    
    # user should input a second card
    while (not isValidInput(userInput,len(valGrid),len(valGrid[0]))):
        userInput = input("Choose a second card to uncover: ").upper()
    # rowTwo and colTwo are the coordinates of the second card
    rowTwo,colTwo = int(userInput[1:]) - 1 , ord(userInput[0]) - ord('A')
    # if the second card is already visible or the second card is the first
    # card, the user made a mistake; make the user try again
    if (visGrid[rowTwo][colTwo] or
        (rowOne == rowTwo and colOne == colTwo)):
        visGrid[rowOne][colOne] = False
        return (inputError(),score)
    # set the second card to be visible
    visGrid[rowTwo][colTwo] = True
    
    # the user was successful if the two cards match, unsuccessful otherwise
    correct = valGrid[rowOne][colOne] == valGrid[rowTwo][colTwo]
    if (correct): score += POINTS_PER_PAIR
    else: score += -1
    display(valGrid,visGrid,score)
    # if the user was unsuccessful, reset the cards' visibility after showing
    # the user the two cards
    if (not correct): visGrid[rowOne][colOne] = visGrid[rowTwo][colTwo] = False
    return (isSolved(visGrid),score)

# prints a message indicating the user gave an invalid card and needs to retry
def inputError():
    print("Invalid card. Try again.")
    return False

# determines if the input is a card
def isValidInput(userInput,rows,cols):
    if (userInput == '?'): info() # if the input is '?', give the user some info
    return (1 <= len(userInput) <= 3 and
            userInput[0].isalpha() and userInput[1:].isnumeric() and
            ord(userInput[0].upper()) - ord('A') < cols and
            int(userInput[1:]) <= rows )

# determines if the game is completed
def isSolved(visGrid):
    # if every card is visible, the game is completed
    for row in range(len(visGrid)):
        if (False in visGrid[row]): return False
    return True

# print info for the user
def info():
    print('''
________________________________________________________________________________
HOW TO START:
playMemoryGame(rows=3,cols=3,seed=None)

GAME INFO:
A grid-based memory game. Pair up all the cards to win.

HOW TO PLAY:
Enter a card's position (ex. a1) to choose that card. If you choose two cards
that have matching values, 5 points are added to your score. If you choose two
cards that have different values, 1 point is subtracted from your score. Find
all pairs of matching cards to finish the game.
________________________________________________________________________________
''')
#                                                                              #
################################################################################

################################################################################
# Tests
################################################################################

PRINT_TEST = False # determines whether to run the print tests
GRAPHICS_TEST = False # determines whether to run the tk window

# print separators
def sep():
    if (PRINT_TEST): print('''
________________________________________________________________________________
''')
def sepBig():
    if (PRINT_TEST): print('''
################################################################################
################################################################################
################################################################################
''')

def testGenerateValues():
    tests = [
    #   (n,     seed,   correctAns                  ),
        (0,     0,      []                          ),
        (0,     1,      []                          ),
        (2,     0,      [1,1]                       ),
        (1,     0,      [0]                         ),
        (3,     0,      [0,1,1]                     ),
        (3,     1,      [1,1,0]                     ),
        (3,     2,      [1,1,0]                     ),
        (3,     6,      [1,0,1]                     ),
        (4,     0,      [2,1,1,2]                   ),
        (4,     1,      [2,1,2,1]                   ),
        (12,    0,      [1,5,5,3,6,2,2,4,3,1,6,4]   ),
        (13,    0,      [1,5,5,3,6,1,2,4,4,2,0,6,3] ),
        ]
    for test in tests:
        ans = generateValues(test[0],test[1])
        print('''\
generateValues(%d, %d) returns:\n''' % (test[0],test[1]))
        print(ans)
        assert(ans == test[-1])
        sep()
    sepBig()

def testIsValidInput():
    tests = [
    #   (userInput, rows,   cols,   correctAns  ),
        ("",        1,      1,      False       ),
        ("a1",      1,      1,      True        ),
        ("A1",      1,      1,      True        ),
        ("a2",      1,      1,      False       ),
        ("b1",      1,      1,      False       ),
        ("a1a",     1,      1,      False       ),
        ("a",       1,      1,      False       ),
        ("1a",      1,      1,      False       ),
        ("a1",      2,      3,      True        ),
        ("a2",      2,      3,      True        ),
        ("a3",      2,      3,      False       ),
        ("b1",      2,      3,      True        ),
        ("b2",      2,      3,      True        ),
        ("c1",      2,      3,      True        ),
        ("c2",      2,      3,      True        ),
        ("d1",      2,      3,      False       ),
        ("z26",     26,     26,     True        ),
        ]
    for test in tests:
        ans = isValidInput(test[0],test[1],test[2])
        print('''\
isValidInput("%s", %d, %d) returns:\n''' % (test[0],test[1],test[2]))
        print(ans)
        assert ans == test[-1]
        sep()
    sepBig()

if (PRINT_TEST):
    testGenerateValues()
    testIsValidInput()
if (GRAPHICS_TEST):
    pass
