def solution(sizes):
    
    max_b = -100
    max_s = -100
    
    for size in sizes:
        
        if size[0] <= size[1]:
            if size[0] >= max_s:
                max_s = size[0]
            if size[1] >= max_b:
                max_b = size[1]
                
        elif size[0] > size[1]:
            if size[1] > max_s:
                max_s = size[1]
            if size[0] > max_b:
                max_b = size[0]
                
                
    answer = max_b*max_s
        
    return answer