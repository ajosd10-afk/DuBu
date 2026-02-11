import sys

input = sys.stdin.readline

N, K = map(int,input().strip().split())

result = []
n_arr = [i for i in range(1,N+1)]
idx= -1

for i in range(N):
    
    for j in range(1, K+1):
        idx += 1
        if idx == N:
            idx = 0
        if n_arr[idx] == 0:
            while n_arr[idx] == 0:
                idx += 1
                if idx == N:
                    idx = 0

    result.append(str(n_arr[idx]))
    n_arr[idx] = 0

print('<',end ='')
print(', '.join(result), end='')
print('>')