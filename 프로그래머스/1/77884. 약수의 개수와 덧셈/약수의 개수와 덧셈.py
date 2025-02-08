def solution(left, right):
    answer = 0
    import math
    for i in range(left, right+1):
        if math.sqrt(i) % 1 == 0 :
            answer -= i
        else : 
            answer += i
    return answer