import math
# import l  # Assuming the 'l' module is imported
from config import the

class RANGE:
    def __init__(self, at, txt, lo, hi=None):
        self.at = at
        self.txt = txt
        self.scored = 0
        self.x = {'lo': lo, 'hi': hi or lo}
        self.y = {}

    def __str__(self):
        return "{{at: {}, scored: {}, txt: '{}', x: {{hi: {}, lo: {}}}, y: {{{}}}}}".format(
            self.at, self.scored, self.txt, self.x['hi'], self.x['lo'],
            ', '.join('{}: {}'.format(k, v) for k, v in self.y.items()))

    def add(self, x, y):
        self.x['lo'] = min(self.x['lo'], x)
        self.x['hi'] = max(self.x['hi'], x)
        self.y[y] = self.y.get(y, 0) + 1

    def show(self):
        lo, hi, s = self.x['lo'], self.x['hi'], self.txt
        if lo == -math.inf:
            return "{} < {}".format(s, hi)
        elif hi == math.inf:
            return "{} >= {}".format(s, lo)
        elif lo == hi:
            return "{} == {}".format(s, lo)
        else:
            return "{} <= {} < {}".format(lo, s, hi)

    def score(self, goal, LIKE, HATE):
        return score(self.y, goal, LIKE, HATE)

    def merge(self, other):
        both = RANGE(self.at, self.txt, self.x['lo'])
        both.x['lo'] = min(self.x['lo'], other.x['lo'])
        both.x['hi'] = max(self.x['hi'], other.x['hi'])
        for t in [self.y, other.y]:
            for k, v in t.items():
                both.y[k] = both.y.get(k, 0) + v
        return both

    def merged(self, other, tooFew):
        both = self.merge(other)
        e1, n1 = self.entropy(self.y)
        e2, n2 = self.entropy(other.y)
        if n1 <= tooFew or n2 <= tooFew:
            return both
        e3, _ = self.entropy(both.y)
        if e3 <= (n1 * e1 + n2 * e2) / (n1 + n2):
            return both
        
    def entropy(self,t):
        n = sum(t.values())
        e = 0
        for v in t.values():
            e -= v / n * math.log2(v / n)
        return e, n
    
def score(t, goal, LIKE, HATE, like=None, hate=None, tiny=None):
    like, hate, tiny = 0, 0, 1E-30
    for klass, n in t.items():
        if klass == goal:
            like += n
        else:
            hate += n
    like, hate = like / (LIKE + tiny), hate / (HATE + tiny)
    if hate > like:
        return 0
    else:
        return like ** the.Support / (like + hate)
