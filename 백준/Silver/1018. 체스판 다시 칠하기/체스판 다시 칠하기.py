import sys

input = sys.stdin.readline

# 1. 입력 받기
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

repair_counts = []

# 2. 전체 보드에서 8x8로 자를 수 있는 시작점(i, j) 탐색
for i in range(N - 7):
    for j in range(M - 7):
        white_start_case = 0 # 맨 왼쪽 위가 'W'인 경우로 가정했을 때 칠할 개수
        black_start_case = 0 # 맨 왼쪽 위가 'B'인 경우로 가정했을 때 칠할 개수

        # 3. 시작점(i, j)으로부터 8x8 칸을 하나씩 검사
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # (행 인덱스 + 열 인덱스)의 합이 짝수이면 시작점과 색이 같아야 함
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        white_start_case += 1
                    if board[a][b] != 'B':
                        black_start_case += 1
                # 합이 홀수이면 시작점과 색이 달라야 함
                else:
                    if board[a][b] != 'B':
                        white_start_case += 1
                    if board[a][b] != 'W':
                        black_start_case += 1
        
        # 두 경우 중 작은 값을 리스트에 추가
        repair_counts.append(white_start_case)
        repair_counts.append(black_start_case)

# 4. 모든 경우 중 가장 작은 값 출력
print(min(repair_counts))