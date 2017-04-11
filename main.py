import neural

b = neural.neural()
f = 0
w = [0, 0, 0, 0]
dw = [0, 0, 0, 0]
k = 0
i = 0
while k < 100:
    for i in range(0, 15):
        v = b.bit(i)
        if b.bool_func(b.bit(i)) == True:
            h = 1
        else:
            h = 0
        g = b.net(f, w, v)
        s = b.check_error(h, g)
        if s != 0:
            dw = b.hoff(v, s)
            w = b.weight(w, dw)
        else:
            print('ok')
    k += 1
print(w)
#print b.bit(15)
#print b.bool_func(b.bit(7))
#print b.net(f, [1, 1, 1, 1], [1, 1, 1, 1])
