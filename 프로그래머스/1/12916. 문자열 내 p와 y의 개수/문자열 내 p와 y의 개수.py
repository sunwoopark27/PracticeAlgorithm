def solution(s):
    countP = 0
    countY = 0
    for i in list(s):
        if i == 'p' or i == 'P':
            countP += 1
        elif i == 'y' or i == 'Y' :
            countY += 1
    if countP != countY :
        return False
    return True