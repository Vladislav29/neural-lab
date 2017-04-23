import second_neural

l = second_neural.second_neural()
errors = 1

while errors != 0:
    errors = 0
    for i in range(0, 15):
        v = l.bit(i) + [1]
        h = l.bool_func(v)
        q = l.net(v)
        g = l.active_func(l.net(v))
        if l.check_error(h, g):
            errors += 1
            l.hoff(v, h - g, g)
print l.get_w()
