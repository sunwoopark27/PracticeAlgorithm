def solution(ineq, eq, n, m):
    answer = 0
    if eq == "!":
        condition =  f"{n} {ineq} {m}" 
    else : 
        condition = f"{n} {ineq}{eq} {m}"
    
    if eval(condition) :
        answer = 1
    return answer