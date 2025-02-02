from itertools import combinations
def solution(number):
    answer = 0
    friends = list(combinations(number, 3))
    for x, y, z in friends:
        if x+y+z == 0:
            answer += 1
    return answer