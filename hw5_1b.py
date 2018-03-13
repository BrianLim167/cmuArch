# 15-112, Summer 2, Homework 5.1b
################################################################################
# Full name: Brian Lim
# Section: B
# Andrew ID: blim2
################################################################################

################################################################################
# 4. interleave(s1, s2) [10 pts][autograded]                                   #
def interleave(s1, s2):
    if (s1 == ""): return s2
    if (s2 == ""): return s1
    return s1[0] + s2[0] + interleave(s1[1:], s2[1:])
#                                                                              #
################################################################################

################################################################################
# 5. isPerfectNumber(n) [10 pts][autograded]                                   #
def isPerfectNumber(n):
    if (n < 0): return False
    if (n == 0): return True
    divSet = divisors(n, int(n**0.5))
    return recursiveSum(divSet) == n

# set of divisors of n that are less than or equal to high and their
# counterparts, except for n itself
def divisors(n, high):
    if (high == 0): return set()
    if (n % high == 0):
        ans = set([high, n//high]) # divisor and its larger counterpart
        ans = ans.union(divisors(n, high-1))
        ans.discard(n) # n itself should not be included
        return ans
    return divisors(n, high-1)

# recursively calculate the sum
def recursiveSum(s):
    if (s == set()): return 0
    return s.pop() + recursiveSum(s)
#                                                                              #
################################################################################

################################################################################
# 6. flatten(L) [20 pts][autograded]                                           #
def flatten(L):
    if (type(L) != list): return L
    if (L == []): return []
    if (type(L[0]) == list): return flatten(L[0]) + flatten(L[1:])
    return [L[0]] + flatten(L[1:])
#                                                                              #
################################################################################

################################################################################
# ignore_rest
################################################################################

################################################################################
# Tests
################################################################################

assertTest = True # determines whether to run the tests

def testInterleave():
    tests = [
    #   (s1,        s2,         expected    ),
        ("pto",     "yhn",      "python"    ),
        ("a#",      "cD!f2",    "ac#D!f2"   ),
        ("",        "",         ""          ),
        ("ace",     "bdfghij",  "abcdefghij"),
        ("qetuiop", "wry",      "qwertyuiop"),
        ]
    for test in tests:
        assert interleave(test[0],test[1]) == test[-1]

def testDivisors():
    tests = [
    #   (n,     expected                ),
        (1,     set()                   ),
        (2,     set([1])                ),
        (3,     set([1])                ),
        (4,     set([1,2])              ),
        (6,     set([1,2,3])            ),
        (12,    set([1,2,3,4,6])        ),
        (24,    set([1,2,3,4,6,8,12])   ),
        ]
    for test in tests:
        assert divisors(test[0], int(test[0]**0.5)) == test[-1]

def testIsPerfectNumber():
    tests = [
    #   (n,     expected    ),
        (0,     True        ),
        (6,     True        ),
        (28,    True        ),
        (496,   True        ),
        (8128,  True        ),
        (-10,   False       ),
        (-1,    False       ),
        (1,     False       ),
        (2,     False       ),
        (9,     False       ),
        (12,    False       ),
        (144,   False       ),
        (9000,  False       ),
        ]
    for test in tests:
        assert isPerfectNumber(test[0]) == test[-1]

def testFlatten():
    tests = [
    #   (L,                     expected            ),
        ([],                    []                  ),
        ([[],[]],               []                  ),
        ([1,[2]],               [1,2]               ),
        ([1,2,[3,[4,5],6],7],   [1,2,3,4,5,6,7]     ),
        (3,                     3                   ),
        ]
    for test in tests:
        assert flatten(test[0]) == test[-1]
        

if (assertTest):
    testInterleave()
    testDivisors()
    testIsPerfectNumber()
    testFlatten()
