def solution(clothes):
    
    def count_case(n):
        return n+1
    
    cloth_list ={}
    
    for i in clothes:
        if cloth_list.get(i[1]) == None:
            cloth_list[i[1]] = 1
        else:
            cloth_list[i[1]] += 1
            
    answer = 1
            
    for j in cloth_list:
        answer *= count_case(cloth_list[j])
    
    answer -= 1
    
    return answer