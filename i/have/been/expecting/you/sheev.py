from sys import stdin


def young_skywalker():
    for cn in xrange(1, 1 + getint()):
        plan = []
        n = getint()
        ps = getints()
        m1 = max((ps[i],i) for i in xrange(n))[1]
        m2 = max((ps[i],i) for i in xrange(n) if i != m1)[1]
        for k in xrange(ps[m1]-ps[m2]):
            plan.append([m1])
        for j in xrange(n):
            if j != m1 and j != m2 and (j+1) != (m1+1):
                for z in xrange(ps[j]):
                    plan.append([j])
        for j in xrange(ps[m2]):
            plan.append([m1,m2])
        print("Case #{}: {}".format(cn, " ".join("".join(chr(65+i) for i in step) for step in plan)))


def getints():
    return tuple(int(z) for z in stdin.readline().split())


def getint():
    # testing to see if comments affect this at all
    return int(stdin.readline())