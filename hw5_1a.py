# 15-112, Summer 2, Homework 5.1a
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

# Keep this function at the top of the file
def almostEqual(d1, d2):
    epsilon = 0.000001
    return abs(d1 - d2) < epsilon

# The start of a very basic Polynomial class...
class Polynomial(object):
    def __init__(self, coeffs):
        # if coeffs == [2,-3,5]:  2x**2-3*x+5
        # @TODO: eliminate leading zero's
        while (coeffs != [] and coeffs[0] == 0): coeffs = coeffs[1:]
        if (coeffs == []): coeffs = [0]
        self.coeffs = coeffs
    
    def degree(self):
        # The degree is power of the largest exponent, and since
        # we start at x**0, this is one less than the number of coefficients.
        return len(self.coeffs)-1
    
    def coeff(self, power):
        # This returns the coefficient corresponding to the given power.
        # Note that these are stored in reverse, in that the coefficient
        # for x**0 is not stored in coeffs[0] but rather coeffs[-1].
        return self.coeffs[self.degree()-power]
    
    def evalAt(self, x):
        # Evaluate this polynomial at the given value of x.
        return sum([self.coeff(power)*x**power
                    for power in range(self.degree()+1)])

    def __add__(self, other):
        # Add this polynomial to another polynomial, producing a third
        # polyonial as the result.  This makes the + operator work right.
        # First, make both coefficent lists the same length by nondestructively
        # adding 0's to the front of the shorter one
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        if (len(coeffs1) > len(coeffs2)):
            (coeffs1, coeffs2) = (coeffs2, coeffs1)
        # Now, coeffs1 is shorter, so add 0's to its front
        coeffs1 = [0]*(len(coeffs2)-len(coeffs1)) + coeffs1
        # Now they are the same length, so add them to get the new coefficients
        coeffs = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs1))]
        # And create the new Polynomial instance with these new coefficients
        return Polynomial(coeffs)

    def __str__(self):
        # Convert this polynomial into a human-readable string.
        # This is not a very good string implementation. Ugly, but functional.
        if (self.degree() == 0): return str(self.coeff(0))
        result = ""
        for power in range(self.degree(), -1, -1):
            coeff = self.coeff(power)
            if (coeff == 0): continue
            sign = abs(coeff)//coeff
            coeff = abs(coeff)
            if (result != ""):
                if (sign == 1): result += " + "
                else: result += " - "
            elif (sign == -1): result += "-"
            if (power == 0 or coeff > 1): result += str(coeff)
            if (power > 0): result += "x"
            if (power > 1): result += "^%d" % power
        return result

    def __eq__(self, other):
        return (isinstance(other, Polynomial) and self.coeffs == other.coeffs or
                type(other) == int and self.coeffs == [other])

    def __hash__(self):
        return hash(tuple(self.coeffs))

    def __mul__(self, other):
        # coeffs list for the product
        mulCoeffs = []
        if (isinstance(other,Polynomial)):
            mulCoeffs = [0] * (len(self.coeffs)+len(other.coeffs))
            for i in range(self.degree(),-1,-1):
                for j in range(other.degree(),-1,-1):
                    mulCoeffs[-1-i-j] += self.coeff(i) * other.coeff(j)
        if (type(other) == int):
            mulCoeffs = [0] * len(self.coeffs)
            for i in range(self.degree(),-1,-1):
                mulCoeffs[-1-i] = self.coeff(i) * other
        return Polynomial(mulCoeffs)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        ans = 1
        for i in range(other):
            ans *= self
        return ans

class Quadratic(Polynomial):
    def determinant(self): # should be called discriminant
        return self.coeff(1)**2 - 4*self.coeff(2)*self.coeff(0)

    def numberOfRealRoots(self):
        if (self.determinant() == 0): return 1
        if (self.determinant() > 0): return 2
        return 0

    def getRealRoots(self):
        ans = []
        a = self.coeff(2)
        b = self.coeff(1)
        roots = self.numberOfRealRoots()
        if (roots > 0):
            ans.append( (-b - self.determinant()**0.5)/(2*a) )
        if (roots == 2):
            ans.append( (-b + self.determinant()**0.5)/(2*a) )
        return ans
        

################################################################################
# ignore_rest
################################################################################

from tkinter import *
import random

class Bird(object):
    def __init__(self,x,y):
        self.color = "brown"
        self.radius = 20
        self.position = x
        self.altitude = y
        self.vel = 0
        self.accel = 5
        self.jumpVel = -18

    def getColor(self):
        return self.color
    def setColor(self, color):
        old = self.color
        self.color = color
        return old

    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        old = self.radius
        self.radius = radius
        return old

    def getPosition(self):
        return self.position
    def setPosition(self, position):
        old = self.position
        self.position = position
        return old

    def getAltitude(self):
        return self.altitude
    def setAltitude(self, altitude):
        old = self.altitude
        self.altitude = altitude
        return old

    def getVel(self):
        return self.vel
    def setVel(self, vel):
        old = self.vel
        self.vel = vel
        return old

    def getAccel(self):
        return self.accel
    def setAccel(self, accel):
        old = self.accel
        self.accel = accel
        return old

    def getJumpVel(self):
        return self.jumpVel
    def setJumpVel(self, jumpVel):
        old = self.jumpVel
        self.jumpVel = jumpVel
        return jumpVel

    def draw(self, canvas):
        x = self.getPosition()
        y = self.getAltitude()
        r = self.getRadius()
        canvas.create_oval(x-r,y-r, x+r,y+r, fill=self.getColor())

    def timerFired(self):
        self.setAltitude(self.getAltitude()+self.getVel())
        self.setVel(self.getVel()+self.getAccel())

    # determines if bird has left the game area
    def isOffScreen(self, data):
        return not (0 <= self.getAltitude() <= data.height)

    def keyPressed(self, event):
        if (event.keysym == "space"): self.setVel(self.getJumpVel())

class Obstacle(object):
    gap = 360
    altitudeVariation = 80
    altitudeMax = 410
    altitudeMin = 10
    def __init__(self,x,y):
        self.color = "green"
        self.size = 100
        self.position = x
        self.altitude = y
        self.vel = -10
        self.opening = 180

    def getColor(self):
        return self.color
    def setColor(self, color):
        old = self.color
        self.color = color
        return old

    def getSize(self):
        return self.size
    def setSize(self, size):
        old = self.size
        self.size = size
        return old

    def getPosition(self):
        return self.position
    def setPosition(self, position):
        old = self.position
        self.position = position
        return old

    def getAltitude(self):
        return self.altitude
    def setAltitude(self, altitude):
        old = self.altitude
        self.altitude = altitude
        return old

    def getVel(self):
        return self.vel
    def setVel(self, vel):
        old = self.vel
        self.vel = vel
        return old

    def getOpening(self):
        return self.opening
    def setOpening(self, opening):
        old = self.opening
        self.opening = opening
        return old
    
    def draw(self, data, canvas):
        color = self.getColor()
        x0 = self.getPosition()
        x1 = self.getPosition() + self.getSize()
        y0 = 0
        y1 = self.getAltitude()
        canvas.create_rectangle(x0,y0, x1,y1, fill=color)
        y0 = self.getAltitude() + self.getOpening()
        y1 = data.height
        canvas.create_rectangle(x0,y0, x1,y1, fill=color)
        
    def timerFired(self):
        self.setPosition(self.getPosition() + self.getVel())

    # determines if bird is touching the obstacle
    def isColliding(self, data):
        bird = data.bird
        x0 = self.getPosition() - bird.getRadius()
        x1 = self.getPosition() + self.getSize() + bird.getRadius()
        if (x0 <= bird.getPosition() <= x1):
            y0 = 0
            y1 = self.getAltitude() + bird.getRadius()
            if (y0 <= bird.getAltitude() <= y1): return True
            y0 = self.getAltitude() + self.getOpening() - bird.getRadius()
            y1 = data.height
            if (y0 <= bird.getAltitude() <= y1): return True
            return False
        return False
 
# Initialize the data which will be used to draw on the screen.
def init(data):
    # load data as appropriate
    data.start = True
    data.startText = '''\

GAME INFO:

Dodge the obstacles as you fly forward.
If you hit an obstacle or leave the screen, you lose!

CONTROLS:

SPACEBAR: Makes the bird jump
R: Restarts the game


PRESS ANY KEY TO CONTINUE
'''
    data.bird = Bird(data.width//4, data.height//2)
    initObstacle = Obstacle(data.width, data.height//2)
    data.obstacles = [initObstacle] 

# These are the CONTROLLERs.
# IMPORTANT: CONTROLLER does *not* draw at all!
# It only modifies data according to the events.
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if (data.start):
        data.start = False
        return
    data.bird.keyPressed(event)
    if (event.keysym == 'r'): init(data) # restart game

def timerFired(data):
    if (data.start):
        return
    data.bird.timerFired()
    if (data.bird.isOffScreen(data)): init(data) # user loses; restart
    for obstacle in data.obstacles:
        obstacle.timerFired()
        if obstacle.isColliding(data): init(data) # user loses; restart
    # if the last obstacle has moved across the desired gap distance, add a new
    # obstacle.
    if (data.obstacles[-1].getPosition() <= data.width - Obstacle.gap):
        altitude = data.obstacles[-1].getAltitude()
        variation= Obstacle.altitudeVariation
        altitude += random.randint(-variation,variation)
        altitude = min(altitude,Obstacle.altitudeMax)
        altitude = max(altitude,Obstacle.altitudeMin)
        data.obstacles.append(Obstacle(data.width, altitude))
    


# This is the VIEW
# IMPORTANT: VIEW does *not* modify data at all!
# It only draws on the canvas.
def redrawAll(canvas, data):
    # draw in canvas
    if (data.start):
        canvas.create_text(data.width//2,data.height//2,
                           text=data.startText, font="Arial 20")
        return
    data.bird.draw(canvas)
    for obstacle in data.obstacles:
        obstacle.draw(data, canvas)


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

################################################################################
# Tests
################################################################################

graphicsTest = True # determines whether to run the tk window
davisTest = True # determines whether to run Professor Davis's tests

if (graphicsTest):
    run(800,600)

# Tests by Professor Davis
def testPolynomialAndQuadraticClasses():
    print("Testing Polynomial and Quadratic classes...")
    for testFn in [testPolynomialBasics,
                   testPolynomialEq,
                   testPolynomialStr,
                   testPolynomialConstructor,
                   testPolynomialInSets,
                   testPolynomialTimesOperator,
                   testPolynomialExponentiationOperator,
                   testQuadraticClass
                  ]:
        print("  Running %s..." % testFn.__name__, end = " ")
        testFn()
        print("Passed!")
    print("Passed all Polynomial and Quadratic Class tests!")
  
def almostEqual(d1, d2):
    epsilon = 0.000001
    return abs(d1 - d2) < epsilon
  
def testPolynomialBasics():
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
    assert(type(p1) == Polynomial)
    assert(p1.degree() == 2)
    assert(p1.coeff(0) == 5)
    assert(p1.coeff(1) == -3)
    assert(p1.coeff(2) == 2)
    assert(p1.evalAt(0) == 5)
    assert(p1.evalAt(2) == 7)
    p2 = Polynomial([4, -3])
    # Now test the + operator
    p3 = p1 + p2 # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
    assert(type(p3) == Polynomial)
    assert(p3.evalAt(2) == 12)
    assert(p3.evalAt(5) == 57)
  
def testPolynomialEq():
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42)
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42)
  
def testPolynomialStr():
    assert(str(Polynomial([1,2,3])) == "x^2 + 2x + 3")
    assert(str(Polynomial([-1,-2,-3])) == "-x^2 - 2x - 3")
    assert(str(Polynomial([42])) == "42")
    assert(str(Polynomial([-42])) == "-42")
    assert(str(Polynomial([0])) == "0")
    assert(str(Polynomial([1,0,-3, 0, 1])) == "x^4 - 3x^2 + 1")
    assert(str(Polynomial([1,0,-3, 0, 1])) == "x^4 - 3x^2 + 1")
    assert(str(Polynomial([-1,0,3, 0, -1])) == "-x^4 + 3x^2 - 1")
  
def testPolynomialConstructor():
    # If the list is empty, treat it the same as [0]
    assert(Polynomial([]) == Polynomial([0]))
    assert(Polynomial([]) != Polynomial([1]))
    # Remove leading 0's
    assert(Polynomial([0,0,0,1,2]) == Polynomial([1,2]))
    assert(Polynomial([0,0,0,1,2]).degree() == 1)
    # Require that the constructor be non-destructive
    coeffs = [0,0,0,1,2]
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    assert(coeffs == [0,0,0,1,2])
  
def testPolynomialInSets():
    s = set()
    assert(Polynomial([1,2,3]) not in s)
    s.add(Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2]) not in s)
  
def testPolynomialTimesOperator():
    # (x**2 + 2)(x**4 + 3x**2) == (x**6 + 5x**4 + 6x**2)
    assert(Polynomial([1,0,2]) * Polynomial([1,0,3,0,0]) ==
           Polynomial([1,0,5,0,6,0,0]))
    # (x**3 - 3x + 5) * 10 == (10x**3 - 30x + 50)
    assert(Polynomial([1,0,-3,5]) * 10 == Polynomial([10,0,-30,50]))
    # Hint: to do multiplication this way, you have to use __rmul__,
    # which should just call __mul__ (yes, really)
    assert(10 * Polynomial([1,0,-3,5]) == Polynomial([10,0,-30,50]))
  
def testPolynomialExponentiationOperator():
    assert(Polynomial([1,2,3])**0 == 1)
    assert(Polynomial([1,2,3])**1 == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3])**2 == Polynomial([1,2,3]) * Polynomial([1,2,3]))
    assert(Polynomial([1,2,3])**3 == Polynomial([1,2,3]) * Polynomial([1,2,3]) * Polynomial([1,2,3]))
  
def testQuadraticClass():
    q1 = Quadratic([3,2,1])  # 3x^2 + 2x + 1
    assert(type(q1) == Quadratic)
    assert(q1.evalAt(10) == 321)
    assert(isinstance(q1, Quadratic) == isinstance(q1, Polynomial) == True)
    # the determinant is b**2 - 4ac
    assert(q1.determinant() == -8)
    # use the determinant to determine how many real roots (zeroes) exist
    assert(q1.numberOfRealRoots() == 0)
    assert(q1.getRealRoots() == [ ])
    # Once again, with a double root
    q2 = Quadratic([1,-6,9])
    assert(q2.determinant() == 0)
    assert(q2.numberOfRealRoots() == 1)
    [root] = q2.getRealRoots()
    assert(almostEqual(root, 3))
    # And again with two roots
    q3 = Quadratic([1,1,-6])
    assert(q3.determinant() == 25)
    assert(q3.numberOfRealRoots() == 2)
    [root1, root2] = q3.getRealRoots() # smaller one first
    assert(almostEqual(root1, -3) and almostEqual(root2, 2))
    # And make sure that these methods were defined in the Quadratic class
    # and not in the Polynomial class (we'll just check a couple of them...)
    assert('evalAt' in Polynomial.__dict__)
    assert('evalAt' not in Quadratic.__dict__)
    assert('determinant' in Quadratic.__dict__)
    assert('determinant' not in Polynomial.__dict__)
  
if (davisTest): testPolynomialAndQuadraticClasses()
