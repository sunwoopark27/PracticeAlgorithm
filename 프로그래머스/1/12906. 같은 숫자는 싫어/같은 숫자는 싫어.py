from collections import deque

def solution(arr):
    answer = deque()
    
    if len(arr) == 1 : 
        return arr
    
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if answer[-1] != arr[i] :
            answer.append(arr[i])
            
    return list(answer)