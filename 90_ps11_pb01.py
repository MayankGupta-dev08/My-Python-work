'''Simple Inheritance Question'''

class C2DVector:
    def __init__(self, i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"   

class C3DVector(C2DVector):
    def __init__(self, i,j,k):
        super().__init__(i,j)
        self.kcap = k
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"   

c3dv = C3DVector(4,5,6)
c2dv = C2DVector(1,2)
print(c3dv)        
print(c2dv)