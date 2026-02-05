import sys
input = sys.stdin.readline

N = int(input())
# 리스트가 아닌 집합(set)으로 바로 저장
N_set = set(map(int, input().strip().split()))

M = int(input())
M_arr = list(map(int, input().strip().split()))

for target in M_arr:
    # set에 값이 있는지 확인 (매우 빠름)
    if target in N_set:
        print(1)
    else:
        print(0)