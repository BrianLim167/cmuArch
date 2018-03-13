# 15-112, Summer 2, Homework 4.1
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

################################################################################
# 1. Better Big Oh [30 pts][manually graded]                                   #
'''
import copy

# O(1); len(a) is a constant time function.
def slow1(a):
    return len(a)

# O(N); list to set conversion takes N time.
def slow2(a):
    return len(a) == len(set(a))

# O(N); in takes constant time for sets, so the for loop that iterates N many
# times takes N time.
def slow3(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    a = set(a)
    result = 0
    for c in b:
        if c not in a:
            result += 1
    return result

# O(N); max(L) and min(L) take N time.
def slow4(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    return max( abs(max(a) - min(b)), abs(max(b) - min(a)) )

# O(NlogN); sorted(L) takes NlogN time; binary search takes logN time, so the
# for loop also takes NlogN time; O(NlogN) + O(NlogN) = O(NlogN).
def slow5(a, b):
    # Hint: this is a tricky one!  Even though it looks syntactically
    # almost identical to the previous problem, in fact the solution
    # is very different and more complicated.
    # You'll want to sort one of the lists,
    # and then use binary search over that sorted list (for each value in
    # the other list).  In fact, you should use bisect.bisect for this
    # (you can read about this function in the online Python documentation).
    # The bisect function returns the index i at which you would insert the
    # value to keep the list sorted (with a couple edge cases to consider, such
    # as if the value is less than or greater than all the values in the list,
    # or if the value actually occurs in the list).
    # The rest is left to you...
    #
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    result = abs(a[0] - b[0])
    a = sorted(a)
    for d in b:
        start = 0
        end = len(a) - 1
        while (start <= end):
            mid = (start + end) // 2
            if (a[mid] == d): return 0
            elif (a[mid] > d): end = mid-1
            else: start = mid + 1
        result = min(result,abs(d-a[mid]))
    return result
'''
#                                                                              #
################################################################################

################################################################################
# 2. invertDictionary(d) [20 pts][autograded]                                  #
def invertDictionary(d):
    ans = dict()
    for key in d:
        # if d[key] doesn't exist in ans yet, map it to set()
        ans[d[key]] = ans.get(d[key],set())
        ans[d[key]].add(key)
    return ans
#                                                                              #
################################################################################

################################################################################
# 3. friendsOfFriends(d)[20 pts][autograded]                                   #
def friendsOfFriends(d):
    ans = dict()
    people = set()
    for key in d:
        people.add(key)
        for friend in d[key]:
            people.add(friend)
    for key in people:
        # friends, if they exist in d
        for friend in d.get(key,set()):
            # friends of friend, if they exist in d
            for fof in d.get(friend,set()):
                # fof cannot be the person in question or any of their direct
                # friends
                if (fof != key and not fof in d[key]):
                    ans[key] = ans.get(key,set()).union(set([fof]))
        ans[key] = ans.get(key,set())
    return ans
#                                                                              #
################################################################################

################################################################################
# ignore_rest
################################################################################

################################################################################
# 4. runFancyWheel(d)[30 pts][manually graded]                                 #
from tkinter import *
import math

def init(data):
    data.radius = 200
    data.vel = 10
    data.color = "blue"
    data.cx = 300
    data.cy = 300
    data.vertices = [0,90,180,270]

def mousePressed(event, data):
    if ( (event.x - data.cx)**2 + (event.y - data.cy)**2 <= data.radius**2 ):
        data.vel *= -1
def keyPressed(event, data):
    degInCircle = 360
    num = len(data.vertices)
    # change number of vertices
    if (event.keysym == "Left" or event.keysym == "Down"):
        num = max(num-1, 2)
    elif (event.keysym == "Right" or event.keysym == "Up"):
        num += 1
    # change color
    elif(event.char == 'r'):
        data.color = "red"
    elif(event.char == 'g'):
        data.color = "green"
    elif(event.char == 'b'):
        data.color = "blue"
    # update data.vertices
    newVertices = []
    for i in range(num):
        newVertices.append(data.vertices[0] + i*degInCircle/num)
    data.vertices = newVertices

def timerFired(data):
    # change vertices' position based on velocity
    for i in range(len(data.vertices)):
        data.vertices[i] += data.vel
        
def redrawAll(canvas, data):
    # draw lines between every two points
    for i in range(len(data.vertices)):
        for j in range(i+1,len(data.vertices)):
            xI = data.cx + data.radius * math.cos(math.radians(data.vertices[i]))
            yI = data.cy + data.radius * math.sin(math.radians(data.vertices[i]))
            xJ = data.cx + data.radius * math.cos(math.radians(data.vertices[j]))
            yJ = data.cy + data.radius * math.sin(math.radians(data.vertices[j]))
            canvas.create_line(xI,yI, xJ,yJ, fill=data.color)
 
def runFancyWheel(width=600, height=600): # by Professor Davis
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
    data.timerDelay = 100 # milliseconds
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
#                                                                              #
################################################################################

################################################################################
# Tests
################################################################################

printTest = False # determines whether to run the print tests
graphicsTest = True # determines whether to run the tk window

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

def testInvertDictionary():
    tests = [
    #   (d,                 correctAns                              ),
        (dict(),            dict()                                  ),
        ({1:2,3:4},         {2:{1},4:{3}}                           ),
        ({1:2,2:3,3:4,5:3}, {2:set([1]), 3:set([2,5]), 4:set([3])}  ),
        ({1:2,2:2,3:2,4:2}, {2:{1,2,3,4}}                           ),
        ]
    for test in tests:
        ans = invertDictionary(test[0])
        if (printTest):
            print('''\
invertDictionary(%s) returns:\n''' % str(test[0]))
            print(ans)
        assert ans == test[-1]
        sep()
    sepBig()

def testFriendsOfFriends():
    tests = [
    #   (d,                             correctAns                              ),
        ({1:{2,3,4,5},
          2:{1,3,6},
          3:set(),4:set(),
          5:set(),6:set()},             {1:{6},2:{4,5},
                                         3:set(),4:set(),
                                         5:set(),6:set()}                       ),
        ({1:{2,3,4},2:{1,3,200,201},
          3:{1,2,4,300},4:{1,3,400},
          200:set(),201:set(),
          300:set(),400:set()},         {1:{200,201,300,400},
                                         2:{4,300},
                                         3:{200,201,400},
                                         4:{2,300},
                                         200:set(),201:set(),
                                         300:set(),400:set()}                   ),
        ({'D': {'B', 'E', 'F'},
          'F': {'D'},
          'E': {'D', 'C'},
          'C': set(),
          'B': {'D', 'E', 'A', 'C'},
          'A': {'D', 'B', 'F'}},        {'D': {'A', 'C'},
                                         'F': {'B', 'E'},
                                         'E': {'B', 'F'},
                                         'C': set(),
                                         'B': {'F'},
                                         'A': {'E', 'C'}}                       ),
        ]
    for test in tests:
        ans = friendsOfFriends(test[0])
        if (printTest):
            print('''\
friendsOfFriends(%s) returns:\n''' % str(test[0]))
            print(ans)
        assert ans == test[-1]
        sep()
    sepBig()

if (printTest):
    testInvertDictionary()
    testFriendsOfFriends()
if (graphicsTest):
    runFancyWheel()
