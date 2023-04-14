class DemoClass:
    """ does this work here with classes?
        yessssss"""
    def __init__(self, a , b, x = 0, y = 0 ):
        self.a = a
        self.b = b
        self.x = x
        self.y = y


cosa = DemoClass("bebe", "caro", 1956, 24)

cosa.z = "agosto"

print(vars(cosa), type(cosa))

bebe = DemoClass(3,"otro", 5)

print(vars(bebe), type(bebe))
