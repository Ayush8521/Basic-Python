'''
create a class (2-D vector) and use it to creatr another class representing
a 3-D vector.
'''
class TwoDVector:
    def _init_(self,i,j):
        self.i = i
        self.j = j

        def show(self):
            print(f"The vector is {self.i}i + {self.j}j ")

class ThreeDVector(TwoDVector):
    def _init_(self, i, j,k):
        super()._init_(i, j)
        self.k = k

    def show(self):
            print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1,2)
a.show()
b = ThreeDVector(1,2,3)
b.show()
