
class Point:
    x: int
    y: int

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Rectangle:
    bottom_left: Point
    top_right: Point
    
    def __init__(self, p1, p2):
        self.bottom_left = p1
        self.top_right = p2
    
    def area(self):
        return (self.top_right.x - self.bottom_left.x) * (self.top_right.y - self.bottom_left.y) 
    
    def dup(self, r):
        bl, tr = Point(0, 0), Point(0, 0)
        if self.bottom_left.x <= r.bottom_left.x < self.top_right.x:
            bl.x = r.bottom_left.x
        elif r.bottom_left.x <= self.bottom_left.x < r.top_right.x:
            bl.x = self.bottom_left.x
        else:
            return None
        
        if self.bottom_left.y <= r.bottom_left.y < self.top_right.y:
            bl.y = r.bottom_left.y
        elif r.bottom_left.y <= self.bottom_left.y < r.top_right.y:
            bl.y = self.bottom_left.y
        else:
            return None

        if self.bottom_left.x < r.top_right.x <= self.top_right.x:
            tr.x = r.top_right.x
        elif r.bottom_left.x < self.top_right.x <= r.top_right.x:
            tr.x = self.top_right.x
        else:
            return None

        if self.bottom_left.y < r.top_right.y <= self.top_right.y:
            tr.y = r.top_right.y
        elif r.bottom_left.y < self.top_right.y <= r.top_right.y:
            tr.y = self.top_right.y
        else:
            return None

        return Rectangle(bl, tr)
        

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        r1 = Rectangle(Point(ax1, ay1), Point(ax2, ay2))
        r2 = Rectangle(Point(bx1, by1), Point(bx2, by2))
        duplicated = r1.dup(r2)
        dup_area = duplicated.area() if duplicated else 0
        return r1.area() + r2.area() - dup_area

         