def solution(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    a = list(map(str,reversed(alpha)))
    answerL = ''
    answerU = ''
    for i in a :
        for j in s :
            if i == j :
                answerL += j
            elif i.upper() == j :
                answerU += j
    answer = answerL + answerU
    return answer