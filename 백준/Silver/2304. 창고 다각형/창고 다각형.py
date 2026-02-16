import sys

input = sys.stdin.readline

# 입력 받기
n = int(input())
pillars = []
for _ in range(n):
    l, h = map(int, input().split())
    pillars.append((l, h))

# 1. 위치(L) 기준으로 정렬
pillars.sort()

# 2. 가장 높은 기둥의 높이와 인덱스 찾기
max_h = 0
max_idx = 0
for i in range(n):
    if pillars[i][1] > max_h:
        max_h = pillars[i][1]
        max_idx = i

total_area = 0

# 3. 왼쪽에서 가장 높은 기둥까지 면적 계산
curr_h = 0
for i in range(max_idx + 1):
    if pillars[i][1] > curr_h:
        curr_h = pillars[i][1]
    
    # 다음 기둥과의 거리만큼 현재 높이로 면적 추가
    if i < max_idx:
        total_area += curr_h * (pillars[i+1][0] - pillars[i][0])

# 4. 오른쪽에서 가장 높은 기둥까지 면적 계산
curr_h = 0
for i in range(n - 1, max_idx - 1, -1):
    if pillars[i][1] > curr_h:
        curr_h = pillars[i][1]
    
    # 이전 기둥(왼쪽 방향)과의 거리만큼 현재 높이로 면적 추가
    if i > max_idx:
        total_area += curr_h * (pillars[i][0] - pillars[i-1][0])

# 5. 가장 높은 기둥 자체의 너비(1) 면적 추가
total_area += max_h

print(total_area)