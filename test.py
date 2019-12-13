class test():
    def __init__(self, code, value):
        self.code=code
        self.value=value

a1 = test('a', 1)
b1 = test('b', 1)
a2 = test('a', 2)

l = [a1, b1, a2]

s = ['a', 'b', 'c']
print('a' in s)
print('v' in s)

print(a1 in l.code)