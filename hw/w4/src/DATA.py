from ROW import ROW
from COLS import COLS
import re,ast,fileinput
import random

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

    def gate(self, budget0, budget, some):
        stats = []
        bests = []
        rows = self.rows[:]  # Copying the list
        random.shuffle(rows)
        
        print("1. top6", [example.cells[5:8] for example in rows[:6]])
        print("2. top50", [example.cells[5:8] for example in rows[:50]])
        rows.sort(key=lambda row: row.d2h(self))
        print("3. most", rows[1].cells[5:8])

        random.shuffle(rows)

        lite = rows[:budget0]
        dark = rows[budget0:]

        for i in range(budget):
            best, rest = self.bestRest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark)
            # print("4: rand", y values of centroid of (from DARK, select BUDGET0+i rows at random))
            print("5: mid:", selected.mid().cells[5:8])
            print("6: top:",best.rows[1].cells[5:8] )
            stats.append(selected.mid())
            bests.append(best.rows[1])
            lite.append(dark.pop(todo))
        return stats, bests

    def bestRest(self, rows, want, best=None, rest=None, top=None):
            rows.sort(key=lambda row: row.d2h(self))

            best, rest = [self.cols.names], [self.cols.names]
            for i, row in enumerate(rows):
                if i < want:
                    best.append(row)
                else:
                    rest.append(row)
            d1 = DATA(0)
            d2 = DATA(0)
            for row in best:
                d1.add(row)
            for row in rest:
                d2.add(row)
            return  d1, d2
    
    def split(self, best, rest, lite, dark):
        selected = DATA(0)
        selected.add(self.cols.names)
        max_val = 1E30
        out = 1

        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            
            if b > r:
                selected.add(row)

            tmp = abs(b + r) / abs(b - r + 1E-300)

            if tmp > max_val:
                out, max_val = i, tmp

        return out, selected

