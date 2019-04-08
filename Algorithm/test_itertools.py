import itertools

def add(op1, op2):
    return op1+op2

def accumulate(iterable, func=add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def combinations(iterable, r):   # equivalent itertools.combinations
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def combinationsP(iterable, r):    # equivalent itertools.combinations
    pool = tuple(iterable)
    n = len(pool)
    perms = itertools.permutations(range(n), r)
    for indices in perms:
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


def combinations_with_replacement(iterable, r):   # equivalent itertools.combinations_with_replacement
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


def combinationsP_with_replacement(iterable, r):  # equivalent itertools.combinations_with_replacement
    pool = tuple(iterable)
    n = len(pool)
    prod = itertools.product(range(n), repeat=r)
    for indices in prod:
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)



def permutations(iterable, r=None):          # equivalent itertools.permutations
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# classmethod chain.from_iterable(iterable)
# Alternate constructor for chain(). Gets chained inputs from a single iterable argument that is evaluated lazily.
def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

import time

L = [1,2,3,4,5,6,7,8,9,10]
cnt = 0
stime = time.time()
for elem in permutations(L):
    cnt += 1

print(cnt)
print(time.time()-stime)

cnt = 0
stime = time.time()
p = list(itertools.permutations(L))
for elem in p:
    cnt += 1
print(cnt)
print(time.time()-stime)
