def solution(arr):
    answer = 0
    before = []
    while True :
        before = arr.copy()
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] / 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = (arr[i] * 2) + 1
            
        if before == arr :
            break
        answer += 1
    return answer
