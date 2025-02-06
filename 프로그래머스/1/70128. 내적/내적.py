def solution(a, b):
    multiplyList = []
    for i,j in zip(a,b):
        multiplyList.append(i * j)  # 곱한 값을 리스트에 추가
    answer = sum(multiplyList)  # 리스트 요소 전체 합산
    return answer
    