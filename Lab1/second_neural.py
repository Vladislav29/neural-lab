import math

class second_neural:

    n = 0.3

    def __init__(self):
        self.w = [0,0,0,0,0]

    def bool_func(self, x):
        return 1 if (x[0] or not(x[1]) or not(x[2] or x[3])) else 0

    def active_func(self, y):
        t = 0
        t = 0.5 * (math.tanh(y) + 1)
        return 1 if y >= 0.5 else 0

    def net(self, x):
        net = 0
        for i in range(0, 4):
            net += self.w[i] * x[i]
        return net + self.w[4]

    def bit(self, n):
        b = 8
        x = []
        while b > 0:
            x.append(0 if n & b == 0 else 1)
            b = b >> 1
        return x

    def check_error(self, t, y):
        return t - y != 0

    def hoff(self, x, b):
        for i in range(len(self.w)):
            self.w[i] += self.n * x[i] * b

    def get_w(self):
        return self.w
