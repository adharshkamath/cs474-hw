(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)

(push)
(define-fun prop () Bool
    (and 
        (or q (not r)) 
        (or (not p) r) 
        (or (not q) r p) 
        (or p q (not q)) 
        (or (not r) q)
    )
)

(check-sat)
(get-model)
(pop)

(push)

(define-fun prop1 () Bool 
    (
        or p (not q)
    )
)

(check-sat)
(get-model)
(pop)

(push)

(define-fun prop2 () Bool 
    (= (and 
        (or q (not r)) 
        (or (not p) r) 
        (or (not q) r p) 
        (or p q (not q)) 
        (or (not r) q)
    )  (or p (not q))
    )
)

(check-sat)
(get-model)
