from ROW import ROW
import math

class NODE:
    def __init__(self, data, lefts=None, rights=None):
        self.here = data
        self.lefts = None
        self.rights = None
        self.left = None
        self.right = None
        self.C = None
        self.cut = None
    
    def new(data):
        return NODE(data)

    def rnd(self, n, ndecs=2):
        if not isinstance(n, (int, float)):
            return n

        if math.floor(n) == n:
            return n

        mult = 10 ** (ndecs or 2)
        return math.floor(n * mult + 0.5) / mult

    def walk(self, fun, depth=0):
        self.depth = depth
        fun(self, depth, not (self.lefts or self.rights))
        if self.lefts:
            self.lefts.walk(fun, depth + 1)
        if self.rights:
            self.rights.walk(fun, depth + 1)

    def d2h(self, data):
        return round(data.mid().d2h(self.here))
    
    def o(self, t, n=None, u=None):
        if isinstance(t, (int, float)):
            return str(round(t, n))
        if not isinstance(t, dict) and not isinstance(t, list):
            return str(t)

        u = []
        for k, v in t.items() if isinstance(t, dict) else enumerate(t):
            if str(k)[0] != "_":
                if len(t) > 0:
                    u.append(self.o(v, n))
                else:
                    u.append(f"${self.o(k, n)}: ${self.o(v, n)}")

        return "{" + ", ".join(u) + "}"
    
    def show(self, max_depth=0):
        
        max_depth = 0
        def _show(node, depth, is_leaf):
            nonlocal max_depth
            post = ""
            if is_leaf:
                post = f"\t{self.o(node.here.mid().cells,2)}"
            else:
                post = ""
            max_depth = max(max_depth, depth)
            print('|.. ' * depth + post)

        self.walk(_show)
        print("")
        print("    " * max_depth,  self.o(self.here.mid().cells,2))
        print("    " * max_depth, "_", str(self.here.cols.names.cells))
