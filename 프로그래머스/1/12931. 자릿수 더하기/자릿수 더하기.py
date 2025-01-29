def solution(n):
    answer = 0
    # 숫자를 리스트로 만듬
    nList = list(map(int,str(n)))
    
    for i in nList:
        answer += i

    return answer