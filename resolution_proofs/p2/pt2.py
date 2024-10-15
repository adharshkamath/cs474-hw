from z3 import *

p = Bool("p")
q = Bool("q")
r = Bool("r")

s = Solver()

s.add(
    Not(
        (
            And(
                (Or(q, Not(r))),
                (Or(Not(p), r)),
                (Or(Not(q), r, p)),
                (Or(p, q, Not(q))),
                (Or(Not(r), q)),
            )
        )
        == (
            And(
                (Or(q, Not(r))),
                (Or(Not(p), r)),
                (Or(Not(q), r, p)),
                (Or(p, q, Not(q))),
                (Or(Not(r), q)),
                (Or(q, Not(p))),
                (Or(p, q, Not(r))),
                (Or(r, Not(q))),
            )
        )
    )
)

if s.check() == unsat:
    # if Not(F) is unsat, F is valid
    # We refer to the formula F when 
    # we say "Formula is valid"
    print("Formula valid!")
else:
    print("Formula not valid")
