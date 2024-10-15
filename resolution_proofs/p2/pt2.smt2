(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)

(define-fun prop1 () Bool 
    (
        or p (not q)
    )
)

(check-sat)
(get-model)
