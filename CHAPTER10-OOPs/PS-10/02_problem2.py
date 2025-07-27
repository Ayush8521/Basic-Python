'''
write a class "calculator" capable of finding square,
cube and square root of a number.
'''


class Calculator:
    def __init__(self, number):
        self.number = number


    def square(self):
        print(f"The square is {self.number*self.number}")

    def cube(self):
        print(f"The cube is {self.number*self.number*self.number}")

    def squareroot(self):
        print(f"The squareroot is {self.number**1/2}")

a = Calculator(4)

a.square()
a.cube()
a.squareroot()

    