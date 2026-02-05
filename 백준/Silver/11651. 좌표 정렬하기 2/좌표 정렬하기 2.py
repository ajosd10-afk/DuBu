import sys

input = sys.stdin.readline

T = int(input())

dot_list = list(tuple(map(int,input().strip().split())) for _ in range(T))

dot_list = sorted(dot_list, key=lambda x: (x[1],x[0]))

for i in dot_list:
    print(f'{i[0]} {i[1]}')