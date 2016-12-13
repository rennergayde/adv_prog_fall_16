class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius**2)*3.14

    def perimeter(self):
        return 2*self.radius*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.radius, self.area(), self.perimeter())

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return (2* self.x) + (2 * self.y)

    def __str__(self):
        return "Rectangle has dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self, x):
        self.x = x
        self.y = x

class Right_Triangle():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hypo = (x**2 + y**2)**(.5)

    def area(self):
        return .5 * self.x * self.y

    def perimeter(self):
        return self.x + self.y + self.hypo

    def __str__(self):
        return "Triangle has dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Isoceles_Right_Triangle(Right_Triangle):
    def __init__(self,x):
        self.x = x
        self.y = x
        self.hypo = (2 * x**2)**(.5)

class Depth():
    def __init__(self, h):
        self.h = h

    def volume(self):
        return self.area() * self.h

    def surface_area(self):
        return 2 * self.area() + self.h * self.perimeter()

class Cube(Square, Depth):
    def __init__(self,x):
        self.x = x
        self.y = x
        self.h = x

class Box(Rectangle, Depth):
    def __init__(self,x,y,h):
        self.x = x
        self.y = y
        self.h = h

class Wedge(Right_Triangle, Depth):
    def __init__(self,x,y,h):
        self.x = x
        self.y = y
        self.hypo = (2 * x**2)**(.5)
        self.h = h

class Cylinder(Circle, Depth):
    def __init__(self,r,h):
        self.radius = r
        self.h = h

j = Cylinder(8,4)
# print j.__str__()
r = Wedge(3,4,7)
# print r.volume()
# print r.surface_area()
g = Box(4,5,6)
#print g.volume()
k = Cube(6)
# print k.surface_area()
# print k.volume()
x = Rectangle(3,4)
# print x
y = Square(5)
# print y
z = Right_Triangle(3,4)
# print z
q = Isoceles_Right_Triangle(3)
# print q
