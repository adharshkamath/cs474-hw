from z3 import *

p = Bool("p")
q = Bool("q")
r = Bool("r")

s = Solver()

s.add(
    (
        And(Or(q, Not(r))),
        (Or(Not(p), r)),
        (Or(Not(q), r, p)),
        (Or(p, q, Not(q))),
        (Or(Not(r), q)),
    )
)


print(s.check())
print(s.model())
