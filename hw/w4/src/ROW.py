import math
from config import the
class ROW:
    def __init__(self, cells):
        self.cells = cells

    def __iter__(self):
        return iter(self.cells)    
    
    
    def like(self, data, n, nHypotheses, prior=None, out=None, v=None, inc=None):
        prior = (len(data.rows) + the['k']) / (n + the['k'] * nHypotheses)
        out = math.log(prior)
        # print(data.cols.x)
        for col in data.cols.x:
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out += 0 if inc ==0 else math.log(inc)
        return math.exp(out)
    
    def likes(self, datas, n=None, nHypotheses=None, most=None, tmp=None, out=None):
        n, nHypotheses = 0, 0
        for _, data in datas.items():
            n += len(data.rows)
            nHypotheses += 1

        for _, data in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, _
                
        return out, most
    
    def d2h(self, data):
        d, n = 0, 0
        for col in data.cols.y:
            n += 1
            d += abs(col.heaven - col.norm(self.cells[col.at])) ** 2
        return (d ** 0.5) / (n ** 0.5)

    # def norm(self, x):
    #     return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)
