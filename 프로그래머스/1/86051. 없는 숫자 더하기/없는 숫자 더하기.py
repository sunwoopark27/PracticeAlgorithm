numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def solution(numbers):
    answer = 0
    for num in numList :
        if num in numbers:
            answer += 0
        else : 
            answer += num
    return answer