import sys

input = sys.stdin.readline

N = int(input().strip()) # 사람 수

time_list = list(map(int, input().strip().split()))

time_list.sort()

sum = 0

for i in range(N,0,-1):
    sum += time_list[abs(i-N)]*i
    
print(sum)