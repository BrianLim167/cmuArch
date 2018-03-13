# 15-112, Summer 2, Homework 1.4
######################################
# Full name: Brian Lim
# Andrew ID: blim2
# Section: B
######################################

######### IMPORTANT NOTE #############
# You are not allowed to use lists, or recursion. 
# And you are not allowed to use any string methods or import the string module.

import math


# See here for details:
# https://www.cs.cmu.edu/~112/notes/quiz2-practice.html#cosineError
def cosineError(x, k):
    cos = 0
    for i in range(k+1):
        sign = i % 2 * -2 + 1 # alternates between 1 and -1 with respect to i5
        cos += x**(i*2)/math.factorial(i*2) * sign
##    print(cos)
    return abs(math.cos(x) - cos)


# See here for details:
# https://www.cs.cmu.edu/~112/notes/hw2-practice.html#isRotation
def isRotation(x, y):
    x = str(x)
    y = str(y)
    while len(x) < len(y):
        x = "0" + x
    while len(y) < len(x):
        y = "0" + y
    for i in range(len(x)):
        if x[i:] + x[:i] == y:
            return True
    return False


# See here for details:
# https://www.cs.cmu.edu/~112/notes/hw2-practice.html#longestDigitRun
def longestDigitRun(n):
    n = abs(n)
    longest = 0
    longestRun = 0
    cur = 0
    curRun = 0
    while n > 0:
        if cur != n % 10:
            cur = n % 10
            curRun = 0
        curRun += 1
        if curRun > longestRun or (curRun == longestRun and cur <= longest):
            longest = cur
            longestRun = curRun
        n //= 10
    return longest
        

####
# helper functions for isType(s) problems
def onlyAlpha(s):
    ans = ""
    for i in range(len(s)):
        if isAlpha(s[i]):
            ans += s[i]
    return ans
def isType(s,minChr,maxChr):
    if len(s) == 0:
        return False
    for i in range(len(s)):
        if (not ord(minChr) <= ord(s[i]) <= ord(maxChr)):
            return False
    return True
######

# Return True if all characters in the string s are digits 
# and there is at least one character. Return False otherwise.
def isDigit(s):
    return isType(s,'0','9')


# Return True if all cased characters in the string s are lowercase 
# and there is at least one cased character. Return False otherwise.
def isLower(s):
    return isType(onlyAlpha(s),'a','z')


# Return True if all alphabetic characters in the string s are uppercase 
# and there is at least one alphabetic character. Otherwise return False.
def isUpper(s):
    return isType(onlyAlpha(s),'A','Z')


# Return True if all characters in the string s are alphabetic 
# and there is at least one character. Return False otherwise.
def isAlpha(s):
    if len(s) == 0:
        return False
    for i in range(len(s)):
        if not (isType(s[i],'a','z') or isType(s[i],'A','Z')):
            return False
    return True

# Return True if all characters in the string s are alphanumeric 
# (i.e. alphabetical character or a digit)
# and there is at least one character. Return False otherwise.
def isAlNum(s):
    if len(s) == 0:
        return False
    for i in range(len(s)):
        if not (isAlpha(s[i]) or isDigit(s[i])):
            return False
    return True


# Input s is assumed to be a string.
# Return a copy of s with all the lowercase letters converted to uppercase.
def toUpper(s):
    ans = ""
    for i in range(len(s)):
        if (isLower(s[i])):
            ans += chr(ord(s[i]) + ord('A') - ord('a'))
        else:
            ans += s[i]
    return ans


# Input s is assumed to be a string.
# Return a copy of s with all the uppercase letters converted to lowercase.
def toLower(s):
    ans = ""
    for i in range(len(s)):
        if (isUpper(s[i])):
            ans += chr(ord(s[i]) + ord('a') - ord('A'))
        else:
            ans += s[i]
    return ans


# Input is assumed to be a pair of strings s and t.
# Return True if string s starts with the string t. Return False otherwise.
# If index is given, the start of s is considered to be the given index.
def startsWith(s, t, index=0):
    s = s[index:]
    if len(s) < len(t):
        return False
    for i in range(len(t)):
        if s[i] != t[i]:
            return False
    return True
        


# Input is assumed to be a pair of strings s and t.
# Return True if string s ends with the string t. Return False otherwise.
def endsWith(s, t):
    if len(s) < len(t):
        return False
    for i in range(-1,-1-len(t),-1):
        if s[i] != t[i]:
            return False
    return True


# Input is assumed to be a pair of strings s and t.
# Return the number of (non-overlapping) occurrences of string t in string s.
def count(s, t):
    if t == "":
        return len(s) + 1
    ans = 0
    while len(s) > 0:
        if startsWith(s, t):
            ans += 1
            s = s[len(t):]
        else: s = s[1:]
    return ans


# Input is assumed to be a pair of strings s and t.
# Return the lowest index in s where the substring t is found.
# If t is not found, return -1.
# If index is given, the start of s is considered to be the given index.
# Hint: use startsWith
def find(s, t, index=0):
    if s == t:
        return 0
    for i in range(len(s)):
        if startsWith(s, t, i):
            return i
    return -1


# The input is assumed to be a string s.
# Return the string s reversed.
# You are not allowed to use string slicing for this function.
# In particular, you can't do s[::-1]
def reverseString(s):
    ans = ""
    for i in range(len(s)-1,-1,-1):
        ans += s[i]
    return ans


# Removes leading and trailing spaces.
# For now we are only considering " " as a space. 
# In particular don't worry about "\n" or "\t".
def strip(s):
    while len(s) > 0 and s[0] == " ":
        s = s[1:]
    while len(s) > 0 and s[-1] == " ":
        s = s[:-1]
    return s


# Return True if string t is a substring of string s, and False otherwise.
# There is actually a built-in operator called "in" that does this
# i.e., (t in s) returns the correct answer.
# But you are not allowed to use the in operator with strings.
def isSubstring(t, s):
    return find(s, t) != -1


# Replace in string s all occurrences of string t1 with string t2.
def replace(s, t1, t2):
    ans = ""
    if t1 == "":
        for i in range(len(s)):
            ans += t2 + s[i]
        ans += t2
        return ans
    while len(s) > 0:
        if startsWith(s, t1):
            ans += t2
            s = s[len(t1):]
        else:
            ans += s[0]
            s = s[1:]
    return ans


# Remove all occurrences of string t from string s.
# Hint: This should be very short.
def remove(s, t):
    return replace(s, t, "")


# Remove all spaces from string s.
# Hint: This should be very short.
def removeSpaces(s):
    return remove(s, " ")



######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

# Make sure every function is tested thoroughly before you submit to Autolab.

def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d1 - d2) < epsilon

def testCosineError():
    print("Testing cosineError()...", end="")
    assert(almostEqual(cosineError(0, 0), abs(math.cos(0) - 1)))
    assert(almostEqual(cosineError(1, 0), abs(math.cos(1) - 1)))
    x = 1.2
    guess = 1 - x**2/2 + x**4/(4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almostEqual(cosineError(x, 2), error))
    x = 0.75
    guess = 1 - x**2/2 + x**4/(4*3*2) - x**6/(6*5*4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almostEqual(cosineError(x, 3), error))
    x = -7
    guess = 1 - x**2/2 + x**4/(4*3*2) - x**6/(6*5*4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almostEqual(cosineError(x, 3), error))
    print("Passed!")

def testIsRotation():
    print("Testing isRotation... ", end="")
    assert(isRotation(0, 0))
    assert(not isRotation(0, 1))
    assert(isRotation(3012, 1230))
    assert(isRotation(3412, 1234))
    assert(isRotation(321, 3210))
    assert(isRotation(3021, 3021))
    print("Passed!")

def testLongestDigitRun():
    print("Testing longestDigitRun... ", end="")
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(10) == 0)
    assert(longestDigitRun(110) == 1)
    assert(longestDigitRun(110011) == 0)
    assert(longestDigitRun(123444444) == 4)
    assert(longestDigitRun(1233442211) == 1)
    assert(longestDigitRun(1233441122) == 1)
    assert(longestDigitRun(65432221115555) == 5)
    assert(longestDigitRun(7866633388888) == 8)
    assert(longestDigitRun(123434) == 1)
    assert(longestDigitRun(122223333) == 2)
    assert(longestDigitRun(-122223333) == 2)
    assert(longestDigitRun(-10) == 0)
    print("Passed!")

def testIsDigit():
    print("Testing isDigit... ", end="")
    assert(not isDigit(""))
    assert(not isDigit(" "))
    assert(not isDigit("ABCD"))
    assert(not isDigit("abcd"))
    assert(isDigit("1234"))
    assert(not isDigit("!*&$"))
    assert(not isDigit("AB12"))
    assert(not isDigit("ab12"))
    assert(not isDigit("!*12"))
    assert(not isDigit("!*ab"))
    assert(not isDigit("!*AB"))
    print("Passed!")

def testIsLower():
    print("Testing isLower... ", end="")
    assert(not isLower(""))
    assert(not isLower(" "))
    assert(not isLower("ABCD"))
    assert(isLower("abcd"))
    assert(not isLower("1234"))
    assert(not isLower("!*&$"))
    assert(not isLower("AB12"))
    assert(isLower("ab12"))
    assert(not isLower("!*12"))
    assert(isLower("!*ab"))
    assert(not isLower("!*AB"))
    assert(not isLower("aB"))
    print("Passed!")

def testIsUpper():
    print("Testing isUpper... ", end="")
    assert(not isUpper(""))
    assert(not isUpper(" "))
    assert(isUpper("ABCD"))
    assert(not isUpper("abcd"))
    assert(not isUpper("1234"))
    assert(not isUpper("!*&$"))
    assert(isUpper("AB12"))
    assert(not isUpper("ab12"))
    assert(not isUpper("!*12"))
    assert(not isUpper("!*ab"))
    assert(isUpper("!*AB"))
    assert(not isUpper("aB"))
    print("Passed!")

def testIsAlpha():
    print("Testing isAlpha... ", end="")
    assert(not isAlpha(""))
    assert(not isAlpha(" "))
    assert(isAlpha("ABCD"))
    assert(isAlpha("abcd"))
    assert(not isAlpha("1234"))
    assert(not isAlpha("!*&$"))
    assert(not isAlpha("AB12"))
    assert(not isAlpha("ab12"))
    assert(not isAlpha("!*12"))
    assert(not isAlpha("!*ab"))
    assert(not isAlpha("!*AB"))
    print("Passed!")

def testIsAlNum():
    print("Testing isAlNum... ", end="")
    assert(not isAlNum(""))
    assert(not isAlNum(" "))
    assert(isAlNum("ABCD"))
    assert(isAlNum("abcd"))
    assert(isAlNum("1234"))
    assert(not isAlNum("!*&$"))
    assert(isAlNum("AB12"))
    assert(isAlNum("ab12"))
    assert(not isAlNum("!*12"))
    assert(not isAlNum("!*ab"))
    assert(not isAlNum("!*AB"))
    print("Passed!")

def testToUpper():
    print("Testing toUpper... ", end="")
    assert(toUpper("") == "")
    assert(toUpper(" ") == " ")
    assert(toUpper("ABCD") == "ABCD")
    assert(toUpper("abcd") == "ABCD")
    assert(toUpper("1234") == "1234")
    assert(toUpper("!*&$") == "!*&$")
    assert(toUpper("AB12") == "AB12")
    assert(toUpper("ab12") == "AB12")
    assert(toUpper("!*12") == "!*12")
    assert(toUpper("!*ab") == "!*AB")
    assert(toUpper("!*AB") == "!*AB")
    print("Passed!")

def testToLower():
    print("Testing toLower... ", end="")
    assert(toLower("") == "")
    assert(toLower(" ") == " ")
    assert(toLower("ABCD") == "abcd")
    assert(toLower("abcd") == "abcd")
    assert(toLower("1234") == "1234")
    assert(toLower("!*&$") == "!*&$")
    assert(toLower("AB12") == "ab12")
    assert(toLower("ab12") == "ab12")
    assert(toLower("!*12") == "!*12")
    assert(toLower("!*ab") == "!*ab")
    assert(toLower("!*AB") == "!*ab")
    print("Passed!")

def testStartsWith():
    print("Testing startsWith... ", end="")
    assert(startsWith("", ""))
    assert(startsWith("a", ""))
    assert(startsWith("a", "a"))
    assert(not startsWith("a", "b"))
    assert(startsWith("aa", "a"))
    assert(startsWith("ab", "a"))
    assert(not startsWith("ba", "a"))
    assert(startsWith("abba", "abba"))
    assert(startsWith("abba", "abb"))
    print("Passed!")

def testEndsWith():
    print("Testing endsWith... ", end="")
    assert(endsWith("", ""))
    assert(endsWith("a", ""))
    assert(endsWith("a", "a"))
    assert(not endsWith("a", "b"))
    assert(endsWith("aa", "a"))
    assert(not endsWith("ab", "a"))
    assert(endsWith("ba", "a"))
    assert(endsWith("abba", "abba"))
    assert(endsWith("abba", "bba"))
    print("Passed!")

def testReverseString():
    print("Testing reverse... ", end="")
    assert(reverseString("") == "")
    assert(reverseString("a") == "a")
    assert(reverseString("aa") == "aa")
    assert(reverseString("ab") == "ba")
    assert(reverseString("aba") == "aba")
    assert(reverseString("abcd") == "dcba")
    print("Passed!")

def testCount():
    print("Testing count... ", end="")
    assert(count("", "") == 1)
    assert(count("", "a") == 0)
    assert(count("abc", "") == 4)
    assert(count("a", "a") == 1)
    assert(count("a", "b") == 0)
    assert(count("aa", "a") == 2)
    assert(count("abbba", "bb") == 1)
    assert(count("abbbba", "bb") == 2)
    assert(count("This is a history test", "is") == 3)
    print("Passed!")

def testFind():
    print("Testing find... ", end="")
    assert(find("", "") == 0)
    assert(find("", "a") == -1)
    assert(find("abc", "") == 0)
    assert(find("a", "a") == 0)
    assert(find("a", "b") == -1)
    assert(find("aa", "a") == 0)
    assert(find("abbba", "bb") == 1)
    assert(find("aabbba", "bb") == 2)
    assert(find("This is a history test", "is") == 2)
    assert(find("Dogs and cats!", "and") == 5)
    assert(find("Dogs and cats!", "or") == -1)
    print("Passed!")

def testStrip():
    print("Testing strip... ", end="")
    assert(strip("") == "")
    assert(strip("a") == "a")
    assert(strip(" a") == "a")
    assert(strip("  a") == "a")
    assert(strip("a ") == "a")
    assert(strip("a  ") == "a")
    assert(strip("  a  ") == "a")
    assert(strip("  a aa  a   a    ") == "a aa  a   a")
    print("Passed!")

def testIsSubstring():
    print("Testing isSubstring... ", end="")
    assert(isSubstring("", ""))
    assert(isSubstring("", "a"))
    assert(isSubstring("a", "a"))
    assert(not isSubstring("a", "b"))
    assert(not isSubstring("aa", "a"))
    assert(isSubstring("abc", "abcd"))
    assert(isSubstring("abc", "xabcx"))
    assert(isSubstring("abc", "xyzabc"))
    assert(not isSubstring("abc", "axbxc"))
    print("Passed!")

def testReplace():
    print("Testing replace... ", end="")
    assert(replace("", "", "") == "")
    assert(replace("a", "", "b") == "bab")
    assert(replace("aaa", "", "b") == "bababab")
    assert(replace("a", "a", " ") == " ")
    assert(replace("hello hi hello", "hello", "hi") == "hi hi hi")
    assert(replace("hello hi hello", "hi", "hello") == "hello hello hello")
    print("Passed!")

def testRemove():
    print("Testing remove... ", end="")
    assert(remove("", "") == "")
    assert(remove("a", "") == "a")
    assert(remove("a", "a") == "")
    assert(remove("aa", "a") == "")
    assert(remove("ab", "a") == "b")
    assert(remove("ab", "b") == "a")
    assert(remove("abba", "b") == "aa")
    assert(remove("abba", "bb") == "aa")
    assert(remove("abcdabcdabcd", "bc") == "adadad")
    assert(remove("abc", "d") == "abc")
    assert(remove("", "d") == "")
    print("Passed!")

def testRemoveSpaces():
    print("Testing removeSpaces... ", end="")
    assert(removeSpaces("") == "")
    assert(removeSpaces(" ") == "")
    assert(removeSpaces("  ") == "")
    assert(removeSpaces(" a") == "a")
    assert(removeSpaces("a ") == "a")
    assert(removeSpaces("  a") == "a")
    assert(removeSpaces("a  ") == "a")
    assert(removeSpaces(" a ") == "a")
    assert(removeSpaces("  a  ") == "a")
    assert(removeSpaces("  a  b  c  ") == "abc")
    print("Passed!")


def testAll():
    testLongestDigitRun()
    testIsRotation()
    testCosineError()
    testIsDigit()
    testIsLower()
    testIsUpper()
    testIsAlpha()
    testIsAlNum()
    testToUpper()
    testToLower()
    testStartsWith()
    testEndsWith()
    testReverseString()
    testCount()
    testFind()
    testStrip()
    testIsSubstring()
    testReplace()
    testRemove()
    testRemoveSpaces()

testAll()

