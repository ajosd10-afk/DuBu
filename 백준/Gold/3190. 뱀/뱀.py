import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
base = [[0] * N for _ in range(N)]

K = int(input().strip())

# 1. 사과 위치 저장 (입력은 1부터 시작하므로 -1 처리)
for _ in range(K):
    app_i, app_j = map(int, input().strip().split())
    base[app_i - 1][app_j - 1] = 3 

L = int(input().strip())

# 2. 방향 전환 정보를 딕셔너리에 저장 (시간: 방향)
dir_info = {}
for _ in range(L):
    x, flag = input().strip().split()
    dir_info[int(x)] = flag

# 뱀 초기 설정
base[0][0] = 1
visit = deque()
visit.append((0, 0))

# 3. 우, 하, 좌, 상 (행렬의 올바른 좌표 이동)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
direc = 0
time = 0

# 4. 방향 지시 횟수(L)와 무관하게 죽을 때까지 무한 루프
while True:
    time += 1
    
    i_idx, j_idx = visit[-1] # 현재 머리 위치
    ni = i_idx + di[direc]
    nj = j_idx + dj[direc]
    
    # 벽에 부딪히지 않았는지 확인
    if 0 <= ni < N and 0 <= nj < N:
        
        # 자기 몸에 부딪힌 경우 종료
        if base[ni][nj] == 1:
            break
            
        # 사과를 먹은 경우 (꼬리 안 줄어듦)
        if base[ni][nj] == 3:
            base[ni][nj] = 1
            visit.append((ni, nj))
            
        # 빈 칸인 경우 (머리 전진, 꼬리 자르기)
        else:
            base[ni][nj] = 1
            visit.append((ni, nj))
            
            tail_i, tail_j = visit.popleft()
            base[tail_i][tail_j] = 0
            
    # 벽에 부딪히면 종료
    else:
        break
        
    # 이동이 끝난 후, 현재 시간에 방향을 바꿔야 하는지 확인
    if time in dir_info:
        if dir_info[time] == 'L':
            direc = (direc + 3) % 4 # 왼쪽 90도
        elif dir_info[time] == 'D':
            direc = (direc + 1) % 4 # 오른쪽 90도

print(time)