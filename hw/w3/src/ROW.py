import math
from config import the
class ROW:
    def __init__(self, cells):
        self.cells = cells

    def __iter__(self):
        return iter(self.cells)
    
    def row_like(self, data, n, nHypotheses, prior, out, v, inc):
        prior = (len(data.rows) + the['k']) / (n + the['k'] * nHypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)
        return math.exp(1) ** out

