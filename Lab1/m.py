import second_neural

b = second_neural.second_neural()
errors = 1

while errors != 0:
    errors = 0
    for i in range(0, 15):
        v = b.bit(i) + [1]
        h = b.bool_func(v)
        g = b.active_func(b.net(v))
        if b.check_error(h, g):
            errors += 1
            b.hoff(v, h - g)
print b.get_w()
