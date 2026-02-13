def solution(answers):
    sum_list = [0, 0, 0]
    
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    idx_1 = 0
    idx_2 = 0
    idx_3 = 0
    
    for ans in answers:
        
        idx_1 = idx_1%5
        idx_2 = idx_2%8
        idx_3 = idx_3%10
        
        if ans == ans_1[idx_1]:
            sum_list[0] += 1
            
        if ans == ans_2[idx_2]:
            sum_list[1] += 1
            
        if ans == ans_3[idx_3]:
            sum_list[2] += 1
            
        idx_1 += 1
        idx_2 += 1
        idx_3 += 1
    
    max_sum = max(sum_list)
    
    answer = []
    
    for i in range(1,4):
        if sum_list[i-1] == max_sum:
            answer.append(i)
    
    return answer