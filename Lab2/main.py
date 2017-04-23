import neural

j = 0
k = 10
errors = 1

b = neural.neural()
c = b.point(-2, 2)
g = b.etalon(c)
print(g)

while errors != 0:
    errors = 0
while j < 10 and k < 20:
    v = b.window(c, j, k)
    m = b.check_error(v, g[k])
    if m:
        errors += 1
        b.hoff(c, m, j, k)
    j += 1
    k += 1
print b.get_w()
