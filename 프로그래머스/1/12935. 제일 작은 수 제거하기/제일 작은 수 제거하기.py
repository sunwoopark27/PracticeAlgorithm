def solution(arr):
    minValue = [min(arr)]
    if len(arr) == 1 :
        return [-1]
    return [x for x in arr if x not in minValue] 