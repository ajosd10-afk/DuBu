import sys
import itertools

input = sys.stdin.readline

T = int(input().strip())
data = [1, 2, 3]

for test_case in range(1, T+1):
    
    n = int(input().strip())
    
    
    result = 0
    for i in range(1, n+1):
        case_arr = list(itertools.product(data, repeat = i))
        
        count = 0
        for case in case_arr:
            sub_sum = 0
            for elem in case:
                sub_sum += elem
                if sub_sum > n:
                    break
            if sub_sum == n:
                count += 1
        
        result += count
    
    print(result)