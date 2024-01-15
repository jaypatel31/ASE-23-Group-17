class ROW:
    def __init__(self, cells):
        self.cells = cells

    def __iter__(self):
        return iter(self.cells)
