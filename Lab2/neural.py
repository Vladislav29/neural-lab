import math
class neural:

    n = 1

    def __init__(self):
        self.w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def point(self, a, b):
        x = []
        l = (float(abs(b)) + float(abs(2 * b - a))) / float(40)
        e = float(2 * b - a)
        while float(b) < e:
            b += l
            x.append(b)
        return x

    def func_activation(self, t):
        return math.exp(t - 1)

    def etalon(self, x):
        y = []
        for i in range(0, 20):
            b = self.func_activation(x[i])
            y.append(b)
        return y

    def hoff(self, x, b, j, k):
        for i in range(j, k):
            self.w[i] += self.n * x[i] * b

    def window(self, x, j, k):
        window = 0
        for i in range(j, k):
            window += x[i] * self.w[i]
        return window

    def check_error(self, x, h):
        return h - x != 0

    def net(self, w, x):
        for i in range(0, 10):
            net = w[i] * x[i] + w[21]
        return net

    def get_w(self):
        return self.w
