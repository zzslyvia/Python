class A():
    """docstring for ClassName"""
    def __init__(self, a,b):
      
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

Count = A(3,5)

print (Count.add())

# print A(5,2).add()


