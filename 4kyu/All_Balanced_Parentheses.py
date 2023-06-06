def balanced_parens(n: int) -> list[str]:
    def res_f(l, r, s):
        if len(s) == n * 2:
            res_m.append(s)
            return
        
        if l < n:
            res_f(l + 1, r, s + '(')
        
        if r < l:
            res_f(l, r + 1, s + ')')
    
    res_m = []
    res_f(0, 0, '')
    return res_m