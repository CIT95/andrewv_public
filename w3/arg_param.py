import sys

def myPrint(value = 4):
    if value == 0:
        print('That can not be a triangle:(')
    elif value == 1:
        print("That is an equilateral triangle")
    elif value == 2:
        print('That is a right triangle')
    elif value == 3:
        print('That is an isosceles triangle')
    elif value == 4:
        print('That a triangle, but there is nothing special about it.')

def isATriangle(side1, side2, side3):
    if not(side1 + side2 > side3) or not(side2 + side3 > side1) or not(side3 + side1 > side2):
        return 0
    elif side1 == side2 == side3:
        return 1
    elif (side1**2 + side2**2 == side3**2) or (side2**2 + side3**2 == side1**2) or (side3**2 + side1**2 == side2**2):
        return 2
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return 3
    else:
        return 4

def die(s = 'BAD INPUT!'):
    print(s)
    sys.exit()

print('Enter the length of 3 sides and i will tell you what kind of triangle they make. (Natural Numbers only)')
side1 = int(input('Enter side 1: '))
if side1 < 1:
    die('Only positive numbers')
side2 = int(input('Enter side 2: '))
if side2 < 1:
    die('Only positive numbers')
side3 = int(input('Enter side 3: '))
if side3 < 1:
    die('Only positive numbers')

myPrint(isATriangle(side1, side2, side3))