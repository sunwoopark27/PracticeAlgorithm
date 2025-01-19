def solution(number, n, m):
    answer = 0
    if number % n == 0 and number % m == 0:
        answer = 1
    return answer

solution(60,2,3)
solution(55,10,5)