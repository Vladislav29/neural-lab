
class neural:
    global x
    global n
    global w
    global f
    global dw
    n = 0.3

    def bool_func(self, x):
        return  bool(x[0]) or not(x[1]) or not(x[2] or x[3])

    def active_func(self, y):
        return 1 if y >= 0.5 else 0

    def bit(self, n):
        b = 8
        x = []
        while b > 0:
            z = n & b
            if z == 0:
                  x.append(0)
            else:
                 x.append(1)
            b = b >> 1
        return x

    def net(self,f, w, x):
        for i in range(0, 4):
            f += w[i] * x[i]
        return f

    def check_error(self, t, y):
        b = t - y
        return b

    def hoff(self, x, b):
        dw = []
        for i in range(0, 3):
            dw[i] = n * b * x[i]
            dw.append(dw[i])
        return dw

    def weight(self, w, dw):
        for i in range(0, 3):
            w[i] = w[i] + dw[i]
            w.append(w[i])
        return w
