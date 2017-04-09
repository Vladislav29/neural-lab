import neural

b = neural.neural()
f = 0
w = [1, 1, 1, 1]
dw = [0, 0, 0, 0]
k = 0
i = 2

if b.bool_func(b.bit(1)) == True:
    h = 1
    print(h)
else:
    h = 0
    print(h)

v = b.bit(i)
g = b.net(f, v, w)
s = b.check_error(h, g)

if s != 0:
    dw.append(b.hoff(v, s))
    w.append(b.weight(w, dw))
    print(dw)
else:
    print('ok')

print g
print v
print s
#print b.bit(15)
#print b.bool_func(b.bit(7))
#print b.net(f, [1, 1, 1, 1], [1, 1, 1, 1])
