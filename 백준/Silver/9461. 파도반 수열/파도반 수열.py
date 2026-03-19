import sys

input = sys.stdin.readline

T = int(input().strip())

sample = [1,1,1,2,2]

for test_case in range(1, T+1):
    
    N = int(input().strip())

    lenth_sample = len(sample)
    
    if N <= lenth_sample:
        result = sample[N-1]
    
    else:
        while N > lenth_sample:
            sample.append(sample[-1]+sample[-5])
            lenth_sample += 1
        
        result = sample[-1]

    print(result)