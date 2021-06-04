'''
Diamond Shape problem in Multiple Inheritance 
                     A
                    / \
                   /   \
                  /     \
                 B       C
                 \      /
                  \    /
                   \  /
                    D
'''

class A:
    def meth(self):
        print("This is a method from class")

class B(A):
    def meth(self):
        print("This is a method from class B")


class C(A):
    def meth(self):
        print("This is a method from class C")


class D(B,C):
    # def meth(self):
        # print("This is a method from class D")
        pass
# Preference fro B over C and D over B,C.

a = A()
b = B()
c = C()
d = D()

d.meth()