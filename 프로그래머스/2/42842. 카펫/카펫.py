import math

def solution(brown, yellow):
    
    answer = []
    divide_num = []
    
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            divide_num.append(i)
            
    for m in divide_num:
        n = yellow//m
        if ((n+2)*2)+(2*m) == brown:
            answer.extend((n+2,m+2))
    
    return answer