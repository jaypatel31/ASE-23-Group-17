import math
from config import the
class ROW:
    def __init__(self, cells):
        self.cells = cells

    def __iter__(self):
        return iter(self.cells)
    
    def like(self, data, n, nHypotheses, prior, out, v, inc):
        prior = (len(data.rows) + the['k']) / (n + the['k'] * nHypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)
        return math.exp(1) ** out
    
    def likes(self, datas, n, nHypotheses, most, tmp, out):
        n, nHypotheses = 0, 0
        for _, data in datas.items():
            n += len(data.rows)
            nHypotheses += 1

        for _, data in datas.items():
            tmp = self.row_like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, _
                
        return out, most


