class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = [], [], []
        self.klass = None

        for at, txt in enumerate(row):
            col = (NUM if txt.isupper() else SYM)(txt, at)
            self.all.append(col)

            if not txt.endswith('X'):
                if txt.endswith(('!', '+', '-')):
                    self.y.append(col)
                    if txt.endswith('!'):
                        self.klass = col
                else:
                    self.x.append(col)

    def add(self, row):
        for cols in [self.x, self.y]:
            for col in cols:
                col.add(row[col.at])
        return row