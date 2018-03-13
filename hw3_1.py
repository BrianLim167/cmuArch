# 15-112, Summer 2, Homework 3.1
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

################################################################################
# 1. bestScrabbleScore(dictionary, letterScores, hand) [40 pts]                #
def bestScrabbleScore(dictionary, letterScores, hand):
    score = 0           # best score found so far
    bestWord = ""       # best word found so far
    bestWordList = [""] # list of tied best words so far
    for word in dictionary:
        # if this word can be made from hand and this word gives a better score
        # than any other words tried, then it is the new bestWord
        newScore = addScore(word, letterScores)
        if (isSubstring(word,hand)):
            if (newScore > score):
                score = addScore(word, letterScores)
                bestWord = word
                bestWordList = [word]
            # if a tie is found, build a list of tied best words
            elif (newScore == score):
                bestWordList.append(word)
    if (score == 0):
        return None
    if (len(bestWordList) == 1): return (bestWord,score)
    return (bestWordList,score)

# True iff word can be formed from the chars in charList
def isSubstring(word,charList):
    superstring = "".join(charList) # string of chars from charList
    for i in range(len(word)):
        if (word[i] in superstring):
            # If a char in word matches a char in superstring,  then remove that
            # char from superstring. This removal ensures that each char in
            # superstring will account for only 1 char in word.
            superstring = superstring.replace(word[i],"",1)
        else:
            # if a char in word does not match a char in superstring, then word
            # cannot be formed
            return False
    return True

# the score that a word is worth according to letterScores, assuming the word is
# valid
def addScore(word, letterScores):
    score = 0
    for i in range(len(word)):
        letter = ord(word[i]) - ord('a')
        score += letterScores[letter]
    return score
#                                                                              #
################################################################################

################################################################################
# 2. solvesCryptarithm(puzzle, solution) [40 pts]                              #
def solvesCryptarithm(puzzle, solution):
    for i in range(len(solution)):
        # replace each letter in puzzle with the corresponding digit according
        # to solution
        puzzle = puzzle.replace(solution[i],str(i)) 
    return isValidArithmetic(puzzle)

def isValidArithmetic(puzzle):
    # changes the string so that the numbers are separated only by '+'s,
    # so that a list of the numbers can be created more easily
    puzzle = puzzle.replace('=','+')
    puzzle = puzzle.split('+')
    # True iff there are 3 elements, all 3 elements are numeric strings, and
    # the numeric sum of the first 2 elements is equal to the 3rd
    numOfElementsInEquation = 3
    return (len(puzzle) == numOfElementsInEquation and
            puzzle[0].isnumeric() and puzzle[1].isnumeric() and
            puzzle[2].isnumeric() and
            int(puzzle[0]) + int(puzzle[1]) == int(puzzle[2]))
#                                                                              #
################################################################################

################################################################################
# 3. isKingsTour(board) [20 pts]                                               #
def isKingsTour(board):
    if (not isValidOrder(board)): return False
    (row,col) = findN(board,1)
    for i in range(2, len(board) ** 2 + 1): # range from 2 to N^2
        coord = findN(board,i)
        if ( abs(row - coord[0]) > 1 or abs(col - coord[1]) > 1 ): return False
        (row,col) = coord
    return True

# True iff board contains exactly one of each number from 1 to N^2
def isValidOrder(board):
    nums = list(range(1, len(board) ** 2 + 1)) # range from 1 to N^2
    for row in range(len(board)):
        for col in range(len(board[row])):
            # removal ensures that each value in nums accounts for only one
            # value in board
            if (board[row][col] in nums): nums.remove(board[row][col])
            else: return False
    return nums == []

# the row and col of an element of board
def findN(board,n):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col] == n): return (row,col)
    return None
#                                                                              #
################################################################################

################################################################################
# ignore_rest
################################################################################

##def rgbString(red, green, blue): # by Paul Davis
##    return "#%02x%02x%02x" % (red, green, blue)
##
##from tkinter import *
## 
##def runDrawing(width=300, height=300):
##    root = Tk()
##    canvas = Canvas(root, width=width, height=height)
##    canvas.pack()
##    root.mainloop()
##    print("bye!")

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

def testIsSubstring():
    tests = [
    #   (word,     charList,            correctAnswer),
        ("",         [],                  True         ),
        ("",         ['a'],               True         ),
        ("qwerty",   list("qwerty"),      True         ),
        ("qwerty",   [],                  False        ),
        ("qwerty",   list("qwert"),       False        ),
        ("qwert",    list("qwerty"),      True         ),
        ("q",        ['q'],               True         ),
        ("q",        list("qqq"),         True         ),
        ("qqq",      ['q'],               False        ),
        ]
    for test in tests:
        ans = isSubstring(test[0],test[1])
        if (PRINT_TEST):
            print('''\
isSubstring("%s", %s) returns:\n''' % (test[0],test[1]) )
            print(ans)
        assert (ans == test[2])
        sep()
    sepBig()

def testAddScore():
    letterScores = [
   #  a, b, c, d, e, f, g, h, i, j, k, l, m
      1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
   #  n, o, p, q, r, s, t, u, v, w, x, y, z
      1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10
   ]
    tests = [
    #   (word,          correctAnswer),
        ("",            0            ),
        ("q",           10           ),
        ("qqq",         30           ),
        ("wwq",         18           ),
        ("wwe",         9            ),
        ("eert",        4            ),
        ("yui",         6            ),
        ("ooooo",       5            ),
        ("qwertyuiop",  27           ),
        ]
    for test in tests:
        ans = addScore(test[0],letterScores)
        if (PRINT_TEST):
            print('''\
addScore("%s",letterScores) returns:\n''' % test[0] )
            print(ans)
        assert (ans == test[1])
        sep()
    sepBig()

def testBestScrabbleScore():
    dictionary = " q qqq wwq wwe eert yui ooooo qwertyuiop e r t rty ytr".split()
    #             10 _30 _18 __9 ___4 __6 ____5 ________27 1 1 1 __6 __6

    
    letterScores = [
   #  a, b, c, d, e, f, g, h, i, j, k, l, m
      1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
   #  n, o, p, q, r, s, t, u, v, w, x, y, z
      1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10
   ]
    
    tests = [
    #   (hand,               correctAnswer     ),
        ([],                   None              ),
        (['w'],                None              ),
        (list("wy"),           None              ),
        (dictionary[0],        (dictionary[0],10)),
        (dictionary[1],        (dictionary[1],30)),
        (dictionary[2],        (dictionary[2],18)),
        (dictionary[3],        (dictionary[3],9 )),
        (dictionary[4],        (dictionary[4],4 )),
        (dictionary[5],        (dictionary[5],6 )),
        (dictionary[6],        (dictionary[6],5 )),
        (dictionary[7],        (dictionary[7],27)),
        (list("qtrwwee"),      (dictionary[2],18)),
        (list("qyiyiupowter"), (dictionary[7],27)),
        (list("ert"),          (["e","r","t"],1 )),
        (list("try"),          (["rty","ytr"],6 )),
        ]
    
    for test in tests:
        ans = bestScrabbleScore(dictionary,letterScores,test[0])
        if (PRINT_TEST):
            print('''\
bestScrabbleScore(dictionary, letterScores,
                  "%s") returns:\n''' % str(test[0]) )
            print(ans)
        assert(ans == test[1])
        sep()
    sepBig()

def testIsValidArithmetic():
    tests = [
    #   (puzzle,            correctAnswer),
        ("1+1=2",           True         ),
        ("1+2=3",           True         ),
        ("1+2=4",           False        ),
        ("9+3=12",          True         ),
        ("20+128=148",      True         ),
        ("32+1609=535",     False        ),
        ]
    for test in tests:
        ans = isValidArithmetic(test[0])
        if (PRINT_TEST):
            print('''\
isValidArithmetic("%s") returns:\n''' % test[0])
            print(ans)
        assert(ans == test[1])
        sep()
    sepBig()

def testSolvesCryptarithm():
    tests = [
    #   (puzzle,            solution,     correctAnswer),
        ("A+B=C",             "-AB-C-----", False        ),
        ("A+B=C",             "-AB-------", False        ),
        ("A+B=C",             "-ABC------", True         ),
        ("A+B=C",             "---A-B--C-", True         ),
        ("AAA+BBB=CCC",       "-AB-C-----", False        ),
        ("AAA+BBB=CCC",       "-AB-------", False        ),
        ("AAA+BBB=CCC",       "-ABC------", True         ),
        ("AAA+BBB=CCC",       "---A-B--C-", True         ),
        ("SEND+MORE=MONEY",   "OMY--ENDRS", True         ),
        
        ]
    for test in tests:
        ans = solvesCryptarithm(test[0],test[1])
        if (PRINT_TEST):
            print('''\
solvesCryptarithm("%s", "%s") returns:\n''' % (test[0],test[1]) )
            print(ans)
        assert(ans == test[2])
        sep()
    sepBig()

def testIsValidOrder():
    tests = [
    #   (board,           correctAnswer),
        ([[3,2,1],
          [6,4,9],
          [5,7,8]],         True         ),
        ([[1,2,3],
          [7,4,8],
          [6,5,9]],         True         ),
        ([[3,2,1],
          [6,4,0],
          [5,7,8]],         False        ),
        ([[ 1,14,15,16],
          [13, 2, 7, 6],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   True         ),
        ([[ 0,14,15,16],
          [13, 2, 7, 6],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   False        ),
        ([[ 1,14,15,17],
          [13, 2, 7, 6],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   False        ),
        ([[ 1,14,15,16],
          [13, 2, 6, 7],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   True         ),
        ]
    for test in tests:
        ans = isValidOrder(test[0])
        if (PRINT_TEST):
            print('''\
isValidOrder(%s) returns:\n''' % str(test[0]) )
            print(ans)
        assert(ans == test[1])
        sep()
    sepBig()

def testFindN():
    tests = [
    #   (board,         n,      correctAnswer),
        ([[3,2,1],
          [6,4,9],
          [5,7,8]],     9,      (1,2)        ),
        ([[1,2,3],
          [7,4,8],
          [6,5,9]],     0,      None         ),
        ([[3,2,1],
          [6,4,0],
          [5,7,8]],     5,      (2,0)        ),
        ]
    for test in tests:
        ans = findN(test[0],test[1])
        if (PRINT_TEST):
            print('''\
findN(%s, %d) returns:\n''' % (str(test[0]),test[1]) )
            print(ans)
        assert(ans == test[2])
        sep()
    sepBig()

def testIsKingsTour():
    tests = [
    #   (board,           correctAnswer),
        ([[3,2,1],
          [6,4,9],
          [5,7,8]],         True         ),
        ([[1,2,3],
          [7,4,8],
          [6,5,9]],         False        ),
        ([[3,2,1],
          [6,4,0],
          [5,7,8]],         False        ),
        ([[ 1,14,15,16],
          [13, 2, 7, 6],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   True         ),
        ([[ 0,14,15,16],
          [13, 2, 7, 6],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   False        ),
        ([[ 1,14,15,17],
          [13, 2, 7, 6],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   False        ),
        ([[ 1,14,15,16],
          [13, 2, 6, 7],
          [12, 8, 3, 5],
          [11,10, 9, 4]],   False         ),
        ]
    for test in tests:
        ans = isKingsTour(test[0])
        if (PRINT_TEST):
            print('''\
isKingsTour(%s) returns:\n''' % str(test[0]) )
            print(ans)
        assert(ans == test[1])
        sep()
    sepBig()

def testHW():
    testIsSubstring()
    testAddScore()
    testBestScrabbleScore()
    testIsValidArithmetic()
    testSolvesCryptarithm()
    testIsValidOrder()
    testFindN()
    testIsKingsTour()

testHW()

if (GRAPHICS_TEST):
    pass
