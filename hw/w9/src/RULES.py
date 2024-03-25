from config import the

class RULES:
    def __init__(self, ranges, goal, rowss):
        self.sorted = []
        self.goal = goal
        self.rowss = rowss
        self.LIKE = 0
        self.HATE = 0
        self.likeHate()
        for range_ in ranges:
            range_.scored = self.score(range_.y)
        self.sorted = self.top(self.trys(self.top(ranges)))

    def likeHate(self):
        for y, rows in self.rowss.items():
            if y == self.goal:
                self.LIKE += len(rows)
            else:
                self.HATE += len(rows)

    def score(self, t):
        return score(t, self.goal, self.LIKE, self.HATE)

    def trys(self, ranges):
        u = []
        for subset in powerset(ranges):
            if subset:
                rule = RULE.new(subset)
                score = self.score(rule.selectss(self.rowss))
                if score > 0.01:
                    u.append(rule)
        return u

    def top(self, t):
        t.sort(key=lambda x: x.scored, reverse=True)
        u = []
        for x in t:
            if x.scored >= t[0].scored * the.Cut:
                u.append(x)
        return u

def powerset(s):
    t = [[]]
    for i in range(len(s)):
        for j in range(len(t)):
            t.append([s[i]] + t[j])
    return t

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