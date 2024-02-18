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
    
    def show(self, _show, maxDepth):

        maxDepth = 0

        def _show(node, depth, leafp):
            nonlocal maxDepth
            # print(type(ROW.d2h(node.here)),type(node.here.mid().cells))
            post = str(self.d2h(node.here).here.rows[leafp]) + "\t" + str(node.here.mid().cells) if leafp else ""
            maxDepth = max(maxDepth, depth)
            print(('|.. ' * (depth+1)) + post)

        self.walk(_show)
        print("there")
        print("    " * maxDepth + str(self.d2h(self.here).here.rows[0].cells), self.here.mid().cells)
        print("    " * maxDepth + "_", self.here.cols.names)
        print("here")


