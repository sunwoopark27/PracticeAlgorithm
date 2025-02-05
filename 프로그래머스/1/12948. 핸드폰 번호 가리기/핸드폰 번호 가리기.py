def solution(phone_number):
    phone = list(phone_number[::-1])
    
    for i in range(4,len(phone)) :
        phone[i] = '*'
        
    phone.reverse()
    answer = ''.join(phone)
        
    return answer