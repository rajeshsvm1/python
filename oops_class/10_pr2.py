class Calculator:
    def __init__(self,a):
        self.a=a
    def square(self):
        b=(self.a)**2
        print(b)
    def cube(self):
        b=(self.a)**3
        print(b)
    def sqrt(self):
        b=(self.a)**(0.5)
        print(b)
    
a=Calculator(9)
a.square()
a.sqrt()
a.cube()