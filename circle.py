class Circle:
    pi = 3.14159265
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius)**2 * self.pi

    def circumference(self):
        return 2 * self.radius * self.pi

q = Circle(input("Radius:"))
print 'Circumference: ' + str(q.area())
print 'Area: ' + str(q.circumference())
