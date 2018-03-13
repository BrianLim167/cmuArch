# 15-112, Summer 2, Homework @@@
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

################################################################################
# 2. nearestKaprekarNumber(n) [30 pts] [autograded]                                  #
from math import floor,ceil

def nearestKaprekarNumber(n):
    delta = 0
    while True:
        # given f and c as floor(n) and ceil(n), respectively, check for
        # Kaprekar numbers at f, c, f-1, c+1, f-2, c+2, f-3, c+3, ... until such
        # a number is found.
        if (isKaprekar(floor(n) - delta)): return floor(n) - delta
        elif (isKaprekar(ceil(n) + delta)): return ceil(n) + delta
        delta += 1

def isKaprekar(n):
    if (n < 0): return False
    left = n**2
    div = 0 # power of 10 that separates n^2 into two parts
    while (left > 0):
        # left and right parts of n^2
        left,right = (n**2) // (10**div),(n**2) % (10**div)
        if (right != 0 and left + right == n): return True
        div += 1
    # 1 is a Kaprekar number
    return n == 1
#                                                                              #
################################################################################

################################################################################
# 3. hasBalancedParentheses(s)[15 pts] [autograded]                            #
def hasBalancedParentheses(s):
    unresolved = 0 # count of number of unresolved open parentheses
    for i in range(len(s)):
        if (s[i] == '('): unresolved += 1
        elif (s[i] == ')'): unresolved -= 1
        # False if there is a ')' with no matching '(' to its left
        if (unresolved < 0): return False
    return unresolved == 0 # '(' and ')' must balance out
#                                                                              #
################################################################################

################################################################################
# 3. unboundedNumberGuessing(n) [30 pts] [autograded]                          #
def unboundedNumberGuessing(n):
    ans,lower,upper = "0",1,1
    if (n == 0): return ans
    if (abs(n) == 1): return ans + ',' + str(n)
    while (abs(n) > upper):
        ans += ',' + str(upper * int(abs(n)/n)) # upper bound * sign of n
        lower = upper
        upper *= 2
    ans += ',' + str(upper * int(abs(n)/n))
    if (abs(n) != upper): # binary search can be skipped if n is already found
        guess = (lower + upper) // 2
        while (abs(n) != guess):
            ans += ',' + str(guess * int(abs(n)/n)) # guess * sign of n
            if (abs(n) < guess):
                upper = guess
            elif (abs(n) > guess):
                lower = guess
            guess = (lower + upper) // 2
        ans += ',' + str(guess * int(abs(n)/n))
    return ans

#                                                                              #
################################################################################

################################################################################
# ignore_rest
################################################################################

################################################################################
# 1. Better Big Oh [15 pts][manually graded]                                   #
import copy

# 1: slow1 determines the capacity of a by keeping a count as a copy of a is
#    popped; it then returns the count.
# 2: copy.copy(L) takes N time; the while loop reaches its condition in N time;
#    since copy.copy(L) and the while loop are independent of each other,
#    together they take N time. slow1 is an O(N) function.
def slow1(a):
    (b, c) = (copy.copy(a), 0)
    while (b != [ ]):
        b.pop()
        c += 1
    return c

# 1: slow 2 returns the sums of the squares of the numbers of occurrences of
#    each distinct element.
# 2: The outer for loop has N iterations; the inner loop has N iterations; the
#    work done in each iteration of the loop takes constant time; as the loops
#    are nested, together they take N^2 time. slow2 is an O(N^2) function.
def slow2(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(n):
            if (a[i] == a[j]):
                count += 1
    return (count == n)

# 1: slow3 returns the number of elements in b that are not in a.
# 2: The for loop has N iterations; checking if c not in a takes N time;
#    together, they take N^2 time. slow3 is an O(N^2) function.
def slow3(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    result = 0
    for c in b:
        if c not in a:
            result += 1
    return result 

# 1: slow4 returns the greatest possible difference between an element of a and
#    an element of b.
# 2: The outer for loop has N iterations; the inner loop has N iterations; the
#    work done in each iteration of the loop takes constant time; as the loops
#    are nested, together they take N^2 time. slow4 is an O(N^2) function.
def slow4(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    result = abs(a[0] - b[0])
    for c in a:
        for d in b:
            delta = abs(c - d)
            if (delta > result):
                result = delta
    return result

# 1: slow5 returns the least possible difference between an element of a and
#    an element of b.
# 2: The outer for loop has N iterations; the inner loop has N iterations; the
#    work done in each iteration of the loop takes constant time; as the loops
#    are nested, together they take N^2 time. slow5 is an O(N^2) function.
def slow5(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    result = abs(a[0] - b[0])
    for c in a:
        for d in b:
            delta = abs(c - d)
            if (delta < result):
                result = delta
    return result
#                                                                              #
################################################################################

################################################################################
# 4. selectionSort and bubbleSort modifications[10 pts] [manually graded]      #
def selectionSort(a):
    n = len(a)
    for startIndex in range(n-1,-1,-1):
        maxIndex = startIndex
        for i in range(0, startIndex):
            if (a[i] > a[maxIndex]):
                maxIndex = i
        (a[maxIndex], a[startIndex]) = (a[startIndex], a[maxIndex])

def bubbleSort(a):
  end = 0
  swapped = True
  while (swapped):
    swapped = False
    for i in range(len(a)-1,end,-1):
        if (a[i] < a[i - 1]):
          (a[i], a[i-1]) = (a[i-1], a[i])
          swapped = True
    end += 1
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

def testIsKaprekar():
    tests = [
    #   (n,     correctAns  ),
        (-1,    False       ),
        (0,     False       ),
        (1,     True        ),
        (2,     False       ),
        (3,     False       ),
        (9,     True        ),
        (44,    False       ),
        (45,    True        ),
        (55,    True        ),
        (99,    True        ),
        (297,   True        ),
        (703,   True        ),
        ]
    for test in tests:
        ans = isKaprekar(test[0])
        if (PRINT_TEST):
            print('''\
isKaprekar(%d) returns:\n''' % test[0])
            print(ans)
        assert ans == test[-1]
        sep()
    sepBig()

def testNearestKaprekarNumber():
    tests = [
    #   (n,     correctAns  ),
        (1,     1           ),
        (45,    45          ),
        (0,     1           ),
        (49,    45          ),
        (49.9,  45          ),
        (50,    45          ),
        (50.1,  55          ),
        (51,    55          ),
        (2223,  2223        ),
        (2728,  2728        ),
        (2475.5,2223        ),
        ]
    for test in tests:
        ans = nearestKaprekarNumber(test[0])
        if (PRINT_TEST):
            print('''\
nearestKaprekarNumber(%0.1f) returns:\n''' % test[0])
            print(ans)
        assert ans == test[-1]
        sep()
    sepBig()

def testHasBalancedParentheses():
    tests = [
    #   (s,             correctAns  ),
        ("",            True        ),
        ("(",           False       ),
        (")",           False       ),
        ("()",          True        ),
        ("()()",        True        ),
        ("())",         False       ),
        ("()(",         False       ),
        (")(",          False       ),
        ("(()())",      True        ),
        ]
    for test in tests:
        ans = hasBalancedParentheses(test[0])
        if (PRINT_TEST):
            print('''\
hasBalancedParentheses("%s") returns:\n''' % test[0])
            print(ans)
        assert ans == test[-1]
        sep()
    sepBig()

def testUnboundedNumberGuessing():
    tests = [
    #   (n,     correctAns                      ),
        (0,     "0"                             ),
        (1,     "0,1"                           ),
        (-1,    "0,-1"                          ),
        (32,    "0,1,2,4,8,16,32"               ),
        (42,    "0,1,2,4,8,16,32,64,48,40,44,42"),
        (-13,   "0,-1,-2,-4,-8,-16,-12,-14,-13" ),
        (-1536, "0,-1,-2,-4,-8,-16,-32,-64,-128,\
-256,-512,-1024,-2048,-1536"                    ),
        ]
    for test in tests:
        ans = unboundedNumberGuessing(test[0])
        if (PRINT_TEST):
            print('''\
unboundedNumberGuessing(%d) returns:\n''' % test[0])
            print(ans)
        assert ans == test[-1]
        sep()
    sepBig()

def testSelectionAndBubbleSorts():
    tests = [
    #   (a,                 correctAns  ),
        ([],                []          ),
        ([1],               [1]         ),
        ([1,2,3],           [1,2,3]     ),
        ([3,2,1],           [1,2,3]     ),
        ([5,4,1,3,2],       [1,2,3,4,5] ),
        ]
    for test in tests:
        temp1 = test[0][:]
        temp2 = test[0][:]
        selectionSort(temp1)
        bubbleSort(temp2)
        if (PRINT_TEST):
            print('''\
selectionSort(%s) results in:\n''' % test[0])
            print(temp1)
            print()
        assert temp1 == test[-1]
        if (PRINT_TEST):
            print('''\
bubbleSort(%s) results in:\n''' % test[0])
            print(temp2)
        assert temp2 == test[-1]
        sep()
    sepBig()

def test():
    testIsKaprekar()
    testNearestKaprekarNumber()
    testHasBalancedParentheses()
    testUnboundedNumberGuessing()
    testSelectionAndBubbleSorts()

if (GRAPHICS_TEST):
    pass

test()
