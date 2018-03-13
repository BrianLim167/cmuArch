# 15-112, Summer 2, Homework 1.1
######################################
# Full name: Brian Lim
# Andrew ID: blim2
# Section: E
######################################
# In your own words, write a sentence saying that you have read every word 
# of the course syllabus and that you fully understand it:
#
# I have read thoroughly the course syllabus in its entirety and
# I understand everything that I have read.
#
#


# For the functions below, erase the "return 42" line and write the
# appropriate piece of code instead.

# Given an integer or float degreesInFahrenheit, convert it to corresponding
# degrees in celsius.
def convertToCelsius(degreesInFahrenheit):
    return (degreesInFahrenheit - 32) * 5/9


# Given an integer or float degreesInCelsius, convert it to corresponding
# degrees in fahrenheit.
def convertToFahrenheit(degreesInCelsius):
    return degreesInCelsius * 9/5 + 32


# Given an integer n, return the absolute value of that integer. 
def absoluteValue(n):
    if (n < 0):
        return n * -1
    else:
        return n


# Given an integer n, return True if n is even and return False otherwise. 
# Hint: use the % operator.
def isEven(n):
    return n % 2 == 0


# If you have written the functions correctly, you should not get any errors
# when you run this file, i.e., you should pass all the tests.


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)

def testConvertToCelsius():
    print("Testing convertToCelsius()...", end="")
    assert(almostEqual(convertToCelsius(0), -17.77777777777777))
    assert(almostEqual(convertToCelsius(32), 0))
    assert(almostEqual(convertToCelsius(50), 10))
    assert(almostEqual(convertToCelsius(86), 30))
    assert(almostEqual(convertToCelsius(-10), -23.33333333333333))
    assert(almostEqual(convertToCelsius(-20), -28.88888888888888))
    print("Passed.")

def testConvertToFahrenheit():
    print("Testing convertToFahrenheit()...", end="")
    assert(almostEqual(convertToFahrenheit(0), 32))
    assert(almostEqual(convertToFahrenheit(10), 50))
    assert(almostEqual(convertToFahrenheit(20), 68))
    assert(almostEqual(convertToFahrenheit(-10), 14))
    assert(almostEqual(convertToFahrenheit(-50), -58))
    print("Passed.")

def testAbsoluteValue():
    print("Testing absoluteValue()...", end="")
    assert(absoluteValue(0) == abs(0))
    assert(absoluteValue(1) == abs(1))
    assert(absoluteValue(-1) == abs(-1))
    assert(absoluteValue(2) == abs(2))
    assert(absoluteValue(-2) == abs(-2))
    assert(absoluteValue(3.14) == abs(3.14))
    assert(absoluteValue(-3.14) == abs(-3.14))
    print("Passed.")

def testIsEven():
    print("Testing isEven()...", end="")
    assert(isEven(0) == True)
    assert(isEven(1) == False)
    assert(isEven(2) == True)
    assert(isEven(3) == False)
    assert(isEven(4) == True)
    assert(isEven(-1) == False)
    assert(isEven(-2) == True)
    assert(isEven(-3) == False)
    assert(isEven(-4) == True)
    assert(isEven(123456) == True)
    print("Passed.")

def testAll():
    testConvertToCelsius()
    testConvertToFahrenheit()
    testAbsoluteValue()
    testIsEven()

testAll()

