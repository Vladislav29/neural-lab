import neural

b = neural.neural()
f = 0
w = [0, 0, 0, 0]
dw = [0, 0, 0, 0]
k = 0
i = 0

if b.bool_func(b.bit(7)) == True:
    print 1
else:
    print 0

while k < 50:
    while i < 15:
        v = b.bit(i)
        h = b.bool_func(v)

print b.bit(15)
print b.bool_func(b.bit(7))
print b.net(f, [1, 1, 1, 1], [1, 1, 1, 1])
