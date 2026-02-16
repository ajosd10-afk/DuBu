import sys

input = sys.stdin.readline

# 1. 빙고판 정보 입력 받기
board = [list(map(int, input().split())) for _ in range(5)]

# 2. 사회자가 부르는 숫자들 입력 받기 (5줄에 걸쳐 들어옴)
calls = []
for _ in range(5):
    calls.extend(list(map(int, input().split())))

# 3. 숫자별 좌표(행, 열)를 미리 저장 (검색 속도 최적화)
pos_dict = {}
for r in range(5):
    for c in range(5):
        pos_dict[board[r][c]] = (r, c)

def check_bingo():
    """현재 보드 상태에서 완성된 빙고 줄의 개수를 반환합니다."""
    lines = 0
    
    # 가로 줄 체크
    for r in range(5):
        if sum(board[r]) == 0:
            lines += 1
            
    # 세로 줄 체크
    for c in range(5):
        if sum(board[r][c] for r in range(5)) == 0:
            lines += 1
            
    # 대각선 체크 1 (좌상단 -> 우하단)
    if sum(board[i][i] for i in range(5)) == 0:
        lines += 1
        
    # 대각선 체크 2 (우상단 -> 좌하단)
    if sum(board[i][4-i] for i in range(5)) == 0:
        lines += 1
        
    return lines

# 4. 사회자가 숫자를 하나씩 부르며 빙고 확인
for i in range(25):
    num = calls[i]
    r, c = pos_dict[num]
    board[r][c] = 0  # 숫자를 지움 (0으로 표시)
    
    # 최소 12개(3줄 완성 최소 조건)는 불렀을 때부터 체크 시작
    if i >= 11:
        if check_bingo() >= 3:
            print(i + 1)  # 사회자가 부른 횟수 출력 (1-based)
            break