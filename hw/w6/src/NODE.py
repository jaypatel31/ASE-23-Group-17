from ROW import ROW

class NODE:
    def __init__(self, data, lefts=None, rights=None):
        self.here = data
        self.lefts = lefts
        self.rights = rights

    def rnd(n, ndecs=2):
        if not isinstance(n, (int, float)):
            return n
        return round(n, ndecs)

    def walk(self, fun, depth=0):
        fun(self, depth, not (self.lefts or self.rights))
        if self.lefts:
            self.lefts.walk(fun, depth + 1)
        if self.rights:
            self.rights.walk(fun, depth + 1)

    def d2h(self, data):
            return self.rnd(data.mid().d2h(self.here))
    
    def show(self, max_depth=0):
        def _show(node, depth, is_leaf):
            post = ""
            if is_leaf:
                d2h_value = self.rnd(node.here.mid().d2h(self.here))
                post = f"{d2h_value}\t{str(node.here.mid().cells)}"
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            print('|.. ' * depth + post)

        self.walk(_show)
        print("")
        print("    " * max_depth, self.rnd(self.here.mid().d2h(self.here)), str(self.here.mid().cells))
        print("    " * max_depth, "_", str(self.here.cols.names))
