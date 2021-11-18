from ast import literal_eval
import re
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        if p1.x > p2.x or p1.y > p1.y:
            raise ValueError('invalid coordinates')
        self.p1 = p1
        self.p2 = p2

    def intersection(self, other):
        #Check rect is above/bellow or to the left/right of other
        if other.p1.x > self.p2.x or other.p2.x < self.p1.x or other.p1.y > self.p2.y or other.p2.y < self.p1.y:
            return False
        return True
    def print(self):
        print(self.p1.x, self.p1.y)
        print(self.p2.x, self.p2.y)

def getInput(val):
    try:
        r1 = literal_eval(re.sub('(\))(\s+)(\()','\g<1>,\g<3>', val))
        rect = Rectangle(Point(r1[0][0], r1[0][1]), Point(r1[1][0], r1[1][1]))
    except ValueError:
        print("Second coordinate must have higher values than the first!")
        print("Please enter the coordinates in the format mentioned")
        return False
    except SyntaxError:
        print("Please enter the coordinates in the format mentioned")
        return False
    except TypeError:
        print("Please enter the coordinates in the format mentioned")
        return False
    return rect

if __name__ == '__main__':
    r1 = False
    while(r1 == False):
        print("Enter coordinates for the lower left and upper right point of the FIRST Rectangle in this format; '(x1,y1) (x2,y2)':")
        i1 = input()
        r1 = getInput(i1)

    r2 = False
    while (r2 == False):
        print(
            "Enter coordinates for the lower left and upper right point of the SECOND Rectangle in this format; '(x1,y1) (x2,y2)':")
        i2 = input()
        r2 = getInput(i2)

    if r1.intersection(r2):
        print('There is an intersection between the first and second rectangle!')
    else:
        print('There is NO intersection between the first and second rectangle!')
