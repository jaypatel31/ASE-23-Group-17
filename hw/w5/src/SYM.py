import math
from config import the

class SYM:
    def __init__(self, s, n):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + (self.has[x] if x in self.has else 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x
        # if the.m ==0:
        #     print(self.n,x)

    def mid(self):
        return self.mode

    def div(self, e):
        e = 0
        for _, v in self.has.items():
            e -= v / self.n * math.log(v / self.n, 2)
        return e

    def small(self):
        return 0
    
    def like(self, x, prior):
        if self.n+the.m == 0:
            # print(self.n)
            return ((self.has.get(x, 0) or 0) + the.m * prior)
        return ((self.has.get(x, 0) or 0) + the.m * prior) / (self.n + the.m)

    def dist(self, x, y):
        return 1 if x == "?" and y == "?" else 0 if x == y else 1



