class Basic:
    def __init__(self, value):
        self.value = value

    def test(self):
        tada = 1
        self.value *= 2


class Coll1(Basic):

    def test(self):
        super().test()
        self.value *= 10
        tada += 1
        print(tada)

class Coll2(Basic):
    pass

c1 = Coll1(1)
c2 = Coll2(2)


c1.test()
print(c1.value)
c2.test()
print(c2.value)