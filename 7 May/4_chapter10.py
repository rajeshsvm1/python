class calculator:
    def __init__(self,number):
        self.number=number

    def square(self):
        print(self.number**2)
    def cube(self):
        print(self.number**3)
    def squareroot(self):
        print(self.number**(1/2))
    
    @staticmethod

    def greet():
        print("*** welcome to best calculator in the world ***")


num1=calculator(25)
num1.greet()
num1.square()
num1.cube()
num1.squareroot()
num1.greet()