'''
write a class 'complex ' to represent complex number , along
with overloaded operators '+' and '*' which adds and multiplies them.

'''
class Complex:
    def _init_(self,r,i):
        self.r = r
        self.i = i

        def _add_(self, c2):
            return Complex(self.r + c2.r, self.i + c2.i)
        
        def __mul__(self, c2):
        # (a+bi)*(c+di) = (ac-bd) + (ad+bc)i
         real = self.r * c2.r - self.i * c2.i
         imag = self.r * c2.i + self.i * c2.r
         return Complex(real, imag)
        
        def _str_(self):
            return f"{self.r} + {self.i}i"
        
        
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)
 