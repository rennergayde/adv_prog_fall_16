class Hello:
    """A simple example class"""
    i = 12

    def __init__(self, x):
        self.data = ["I", "Love", "Classes!"]
        self.x = x

    def f(self):
        return 'Hello World!!!!!!!!!'

    def add(self):
        return self.x + 1

    def addi(self):
        return self.x + self.i


y = Hello(1)
print y.f()
print y.i
print y.data
print y.add()
print y.addi()
