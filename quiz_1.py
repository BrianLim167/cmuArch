y = 100
def ct1(x,y):
    for i in range(1,x,3):
        if (i%2 == 0):
            print("A:",i,end = " ")
        elif (i%10 == y%10): print("C:",i,y, end = "")
        if ((i**(0.5)) % 1 == 0):
            print("B:",i, end = " ")
        print()
        y += 1

ct1(10,5)
print(y)

def ct2(x):
    y = 5
    for z in range(x+y, 10, -2):
        if (z>20): print('z',z,end = ' ')
        elif (z//10 == z%10): print('z',z,end = ' ')
        for w in range(z,20,y):
            y += 1
            if (w % 10 == 8): print('w',w, end = ' ')
print(ct2(8))
