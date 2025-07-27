'''
write a class vector representing a vector of n dimensions.
overload the + and * operator which calculates the sum and the dot(.) product of them.

'''
class vector:
    def _init_(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def _add_(self, other):
        result = vector(self.x+other.x,self.y + other.y, self.z + other.z)
        return result
    
    def _mul_(self,other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def _str_(self):
        return f"vector({self.x},{self.y},{self.z})"
    
# Test the implementation
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)

print(v1 + v2)    #output: vector(5,7,9)
print(v1 * v2)    #output: 32

print(v1 + v3)    #output: vector(8,10,12)
print(v1 * v3)    #output: 50
