
class neural:
    global x
    global n
    global w

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

    def check_error(self):
        b = t - y
        return b

    def hoff(self, w, iter):
         dw[i] = n * b * x[i]
         return dw

    def weight(self):
        w[i+1] = w[i] + dw[i]
        return w
