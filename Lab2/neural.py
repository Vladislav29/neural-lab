import math
class neural:

    def __init__(self):
        self.w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    def point(self, a, b):
        x = []
        l = (float(abs(a)) + float(abs(b))) / 20
        while a < b:
            a = a + l
            print a
            x.append(a)
        return x

    def func_activation(self, t):
        return math.exp(t - 1)

    def etalon(self, x):
        y = []
        for i in range(0, 20):
            b = self.func_activation(x[i])
            y.append(b)
        return y

    def hoff(self, x, b):
        for i in range(len(self.w)):
            self.w[i] += self.n * x[i] * b

    def window(self, x, w):
        for i in range(0,9):
            h += x[i] * self.w[i] + w[10]
        return h

    def check_error(self, h, g):
        return h - g

    def net(self, w, x):
        for i in range(0, 10):
            net = w[i] * x[i] + w[10]
        return net

    def get_w(self):
        self.w
