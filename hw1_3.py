# 15-112, Summer 2, Homework 1.3
######################################
# Full name: Brian Lim
# Andrew ID: blim2
# Section: B
######################################

######### IMPORTANT NOTE #############
# You are not allowed to import any modules, or use strings, lists, or recursion.


# Definition: For a positive integer n, n factorial, denoted n!,
# is the product n*(n-1)*(n-2)*...*1. If n = 0, then define 0! as 1.
# Given an integer n (which you can assume is non-negative),
# return n! (n factorial).
def factorial(n):
    ans = 1
    for ind in range(n):
        ans *= ind + 1
    return ans

# Definition: We say that m is a factor of n if m divides n without a remainder.
# Given an integer n (which you can assume is positive),
# return the smallest factor of n larger than 1.
# If n is 1, then you should return 1.
def smallestFactor(n):
    if n == 1:
        return 1
    for ind in range(n):
        if ind != 0 and n % (ind + 1) == 0:
            return ind + 1


# Given an integer n (which you can assume is positive),
# return the largest factor of n less than n.
# If n is 1, then you should return 1.
def largestFactor(n):
    if n == 1:
        return 1
    for ind in range(n):
        if ind != 0 and n % (n - ind) == 0:
            return n - ind


# Given an integer n, return the number of digits of n.
def digitCount(n):
    if n == 0:
        return 1
    ans = 0
    n = abs(n)
    while n > 0:
        ans += 1
        n //= 10
    return ans


# Given an integer n, return the sum of its digits.
def digitSum(n):
    ans = 0
    n = abs(n)
    while n > 0:
        ans += n % 10
        n //= 10
    return ans



# A number is cool if the sum of its digits is divisible by 5.
# Given an integer n, return the nth cool number. 
def nthCool(n):
    cools = 0
    num = -1
    while cools <= n:
        num += 1
        if digitSum(num) % 5 == 0:
            cools += 1
    return num


# Given a non-negative integer n, return the integer consisting of exactly n 1's.
# So nOnes(0) == 0, nOnes(1) == 1, nOnes(2) == 11, nOnes(3) == 111, and so on.
def nOnes(n):
    ans = 0
    for ind in range(n):
        ans += 10 ** ind
    return ans

# The input is two numbers base and exp. You can assume exp is an int but base can be a float. 
# Return base**exp. You are not allowed to use the built-in operator ** or the function pow.
def myPower(base, exp):
    ans = 1
    if exp < 0:
        base = 1 / base
        exp *= -1
    for ind in range(exp):
        ans *= base
    return ans


# Read the first paragraph of:
# https://en.wikipedia.org/wiki/Happy_number 
# After some thought, we see that no matter what number we start with, 
# when we keep replacing the number by the sum of the squares of its digits, 
# we'll always either arrive at 4 (unhappy) or at 1 (happy).
# Given an integer n, return True if n is happy, and False otherwise.
# Note that all numbers less than 1 are not happy.
def isHappyNumber(n):
    if n < 1:
        return False
    while n != 1 and n != 4:
        temp = 0
        while n > 0:
            temp += (n % 10)**2
            n //= 10
        n = temp
    return n == 1


# If you have written the functions correctly, you should not get any errors
# when you run this file, i.e., you should pass all the tests.

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

import math

def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

def testFactorial():
    print("Testing factorial()...", end="")
    assert(factorial(0) == math.factorial(0))
    assert(factorial(1) == math.factorial(1))
    assert(factorial(2) == math.factorial(2))
    assert(factorial(3) == math.factorial(3))
    assert(factorial(4) == math.factorial(4))
    assert(factorial(5) == math.factorial(5))
    assert(factorial(10) == math.factorial(10))
    print("Passed.")

def testSmallestFactor():
    print("Testing smallestFactor()...", end="")
    assert(smallestFactor(1) == 1)
    assert(smallestFactor(2) == 2)
    assert(smallestFactor(3) == 3)
    assert(smallestFactor(4) == 2)
    assert(smallestFactor(5) == 5)
    assert(smallestFactor(6) == 2)
    assert(smallestFactor(7) == 7)
    assert(smallestFactor(8) == 2)
    assert(smallestFactor(9) == 3)
    assert(smallestFactor(251*991) == 251)
    print("Passed.")

def testLargestFactor():
    print("Testing largestFactor()...", end="")
    assert(largestFactor(1) == 1)
    assert(largestFactor(2) == 1)
    assert(largestFactor(3) == 1)
    assert(largestFactor(4) == 2)
    assert(largestFactor(5) == 1)
    assert(largestFactor(6) == 3)
    assert(largestFactor(7) == 1)
    assert(largestFactor(8) == 4)
    assert(largestFactor(9) == 3)
    assert(largestFactor(251*991) == 991)
    print("Passed.")

def testDigitCount():
    print("Testing digitCount()...", end="")
    assert(digitCount(0) == 1)
    assert(digitCount(1) == 1)
    assert(digitCount(9) == 1)
    assert(digitCount(10) == 2)
    assert(digitCount(1001) == 4)
    assert(digitCount(999) == 3)
    assert(digitCount(-1) == 1)
    assert(digitCount(-123) == 3)
    assert(digitCount(-123456789) == 9)
    print("Passed.")

def testDigitSum():
    print("Testing digitSum()...", end="")
    assert(digitSum(0) == 0)
    assert(digitSum(1) == 1)
    assert(digitSum(2) == 2)
    assert(digitSum(11) == 2)
    assert(digitSum(111) == 3)
    assert(digitSum(123) == 6)
    assert(digitSum(123456789) == sum(range(10)))
    assert(digitSum(-1) == 1)
    assert(digitSum(-2) == 2)
    assert(digitSum(-123456789) == sum(range(10)))
    print("Passed.")

def testNthCool():
    print("Testing nthCool()...", end="")
    assert(nthCool(0) == 0)
    assert(nthCool(1) == 5)
    assert(nthCool(2) == 14)
    assert(nthCool(3) == 19)
    assert(nthCool(4) == 23)
    assert(nthCool(5) == 28)
    assert(nthCool(9) == 46)
    print("Passed.")

def testNOnes():
    print("Testing nOnes()...", end="")
    assert(nOnes(0) == 0)
    assert(nOnes(1) == 1)
    assert(nOnes(2) == 11)
    assert(nOnes(3) == 111)
    assert(nOnes(4) == 1111)
    assert(nOnes(15) == 111111111111111)
    print("Passed.")

def testMyPower():
    print("Testing myPower()...", end="")
    assert(myPower(0,0) == pow(0,0))
    assert(myPower(0,1) == pow(0,1))
    assert(myPower(1,0) == pow(1,0))
    assert(myPower(1,1) == pow(1,1))
    assert(myPower(2,0) == pow(2,0))
    assert(myPower(0,2) == pow(0,2))
    assert(myPower(2,1) == pow(2,1))
    assert(myPower(1,2) == pow(1,2))
    assert(myPower(10,5) == pow(10,5))
    assert(myPower(3,10) == pow(3,10))
    assert(myPower(1,-1) == pow(1,-1))
    assert(myPower(2,-1) == pow(2,-1))
    assert(myPower(1,-2) == pow(1,-2))
    assert(almostEqual(myPower(10,-5), pow(10,-5)))
    assert(almostEqual(myPower(3,-10), pow(3,-10)))
    assert(almostEqual(myPower(1/10,-5), pow(1/10,-5)))
    assert(almostEqual(myPower(1/3,-10), pow(1/3,-10)))
    assert(almostEqual(myPower(-1/10,-5), pow(-1/10,-5)))
    assert(almostEqual(myPower(-1/3,-10), pow(-1/3,-10)))
    print("Passed.")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed.")

def testAll():
    testFactorial()
    testSmallestFactor()
    testLargestFactor()
    testDigitCount()
    testDigitSum()
    testNthCool()
    testNOnes()
    testMyPower()
    testIsHappyNumber()

testAll()


