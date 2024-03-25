class RULE:
    def __init__(self, ranges):
        self.parts = {}
        self.scored = 0
        for range_ in ranges:
            t = self.parts.get(range_.txt, [])
            t.append(range_)
            self.parts[range_.txt] = t

    def _or(self, ranges, row):
        x = row.cells[ranges[0].at]
        if x == "?":
            return True
        for range_ in ranges:
            lo, hi = range_.x['lo'], range_.x['hi']
            if lo == hi and lo == x or lo <= x < hi:
                return True
        return False

    def _and(self, row):
        for ranges in self.parts.values():
            if not self._or(ranges, row):
                return False
        return True

    def selects(self, rows):
        t = []
        for row in rows:
            if self._and(row):
                t.append(row)
        return t

    def selectss(self, rowss):
        t = {}
        for y, rows in rowss.items():
            t[y] = len(self.selects(rows))
        return t

    def show(self):
        ands = []
        for ranges in self.parts.values():
            ors = [_showLess(range_) for range_ in ranges]
            at = ors[0].at
            ors = [range_.show() for range_ in ors]
            ands.append(" or ".join(ors))
        return " and ".join(ands)

def _showLess(t, ready=False):
    if not ready:
        t = l.copy(t)  # important, since we are about to mess up the y counts
        t.sort(key=lambda a: a.x['lo'])

    i, u = 0, []
    while i < len(t):
        a = t[i]
        if i < len(t) - 1:
            if a.x['hi'] == t[i + 1].x['lo']:
                a = a.merge(t[i + 1])  # warning. the y counts now may be very wrong
                i += 1
        u.append(a)
        i += 1

    return t if len(u) == len(t) else _showLess(u, True)

