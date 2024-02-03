import math
from config import the
import re

# Numerics
class NUM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = 0 if re.search(r"-$", s or "") else 1

    def add(self, x):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.n < 2 else math.sqrt(self.m2 / (self.n - 1))

    def small(self):
        return the.cohen * self.div()

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)
    
    def like(self, x, nom=None, denom=None):
        mu, sd = self.mid(), (self.div() + 1E-30)
        nom = math.exp(-0.5 * (x - mu)**2 / (sd**2))
        denom = sd * 2.5 + 1E-30
        return nom / denom
    
    def dist(self, x, y):
        if x == "?" and y == "?":
            return 1
        x, y = self.norm(x), self.norm(y)
        if x == "?":
            x = 1 if y < 0.5 else 0
        if y == "?":
            y = 1 if x < 0.5 else 0
        return abs(x - y)
    
  


