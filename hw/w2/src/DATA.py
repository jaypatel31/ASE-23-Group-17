from ROW import ROW
from COLS import COLS

class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None

    def add(self, t, fun=None):
        row = t if isinstance(t, ROW) else ROW(t)

        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)  

    # The following methods need the implementation of mid, div, small, and stats 
    # methods in the respective classes they are called on
    def mid(self, cols=None):
        u = [col.mid() for col in (cols or self.cols.all)]
        return ROW(u)

    def div(self, cols=None):
        u = [col.div() for col in (cols or self.cols.all)]
        return ROW(u)

    def small(self):
        u = [col.small() for col in self.cols.all]
        return ROW(u)

    def stats(self, cols=None, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        for col in (self.cols[cols or "y"]):
            u[col.txt] = round(col.get(fun or "mid"), ndivs)
        return u
