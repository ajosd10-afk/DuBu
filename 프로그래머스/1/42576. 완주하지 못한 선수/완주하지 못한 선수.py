def solution(participant, completion):
    
    part = sorted(participant)
    comp = sorted(completion)
    
    p_idx = 0
    c_idx = 0
    answer = None
    
    while True:
        
        if len(comp) == 0:
            answer = part[p_idx]
            break
        
        if part[p_idx] == comp[c_idx]:
            pass
        
        elif part[p_idx] != comp[c_idx]:
            answer = part[p_idx]
            break
            
        if c_idx == len(comp) - 1:
            answer = part[p_idx + 1]
            break
            
        p_idx += 1
        c_idx += 1
        
    return answer