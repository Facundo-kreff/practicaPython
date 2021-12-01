import random
class Papa:
    def __init__(self, boba):
        self.boba=boba

b = Papa("boba")
c = Papa("bob")
d = Papa("boa")
e = Papa("bo")
a = [b.boba,c,d,e]
print(len(a))
print(a)