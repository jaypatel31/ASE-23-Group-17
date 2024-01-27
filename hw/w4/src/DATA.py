from ROW import ROW
from COLS import COLS
import re,ast,fileinput

class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None

    def new(cls, src, fun=None):
        instance = cls()
        if isinstance(src, str):
            for x in cls.csv(src):
                instance.add(x, fun)
        else:
            for x in (src or []):
                instance.add(x, fun)
        return instance

    def add(self, t, fun=None):
        row = t if isinstance(t, ROW) else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)  

    def coerce(s):
        try: return ast.literal_eval(s)
        except Exception: return s
    def csv(file="-"):
        with  fileinput.FileInput(None if file=="-" else file) as src:
            for line in src:
                line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
                if line: yield [coerce(x) for x in line.split(",")]

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

    def stats(self, cols=None, fun=None, ndivs=2):
        u = {".N": len(self.rows)}
        col_name = cols if cols else self.cols.all
        for col in (col_name):
            u[col.txt] = round(float(col.mid()), ndivs) if isinstance(col.mid(), (int, float)) else col.mid()
        return u

    def best_rest(self, rows, want, best, rest, top):
            rows.sort(key=lambda row: row.d2h(self))
            best, rest = [self.cols['names']], [self.cols['names']]
            for i, row in enumerate(rows):
                if i < want:
                    best.append(row)
                else:
                    rest.append(row)
            return  DATA.new(best), DATA.new(rest)
