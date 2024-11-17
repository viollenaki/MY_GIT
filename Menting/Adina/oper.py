class MathOperations:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    
    def division(self):
        return self.a / self.b  
    
    def multiply(self):
        return self.a * self.b
    
    def find_root(self):
        from math import sqrt
        return sqrt(self.a), sqrt(self.b)
    
operations = MathOperations(4,5)

print(operations.add())
print(operations.subtract())
print(operations.division())
print(operations.multiply())
print(operations.find_root())


