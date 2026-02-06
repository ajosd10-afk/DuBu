import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().strip().split()))

M = int(input())
M_list = list(map(int,input().strip().split()))

count_dict = defaultdict(int)
result = []

for i in N_list:
    count_dict[i] += 1

for j in M_list:
    result.append(count_dict[j])

print(*result)