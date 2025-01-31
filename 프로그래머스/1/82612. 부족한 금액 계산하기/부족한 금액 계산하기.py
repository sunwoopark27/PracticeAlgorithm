def solution(price, money, count):
    need = 0
    for i in range(1,count+1):
        need += price*i
    if need <= money :
        return 0
    return need - money