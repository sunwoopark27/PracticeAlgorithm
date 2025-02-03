def solution(x):
    xlist = list(map(int,str(x)))
    sumx = 0
    for i in xlist :
        sumx += i
    if x % sumx == 0:
        answer = True
    else :
        answer = False
    return answer