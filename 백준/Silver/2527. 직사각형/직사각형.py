import sys

# 입력을 빠르게 받기 위해 정의
input = sys.stdin.readline

# 총 4개의 테스트 케이스 처리
for _ in range(4):
    data = list(map(int, input().split()))
    
    # 첫 번째 직사각형 (x1, y1) ~ (p1, q1)
    x1, y1, p1, q1 = data[0:4]
    # 두 번째 직사각형 (x2, y2) ~ (p2, q2)
    x2, y2, p2, q2 = data[4:8]

    # x축과 y축 각각 겹치는 구간의 길이를 계산
    # 겹치는 구간의 시작점은 큰 쪽, 끝점은 작은 쪽 선택
    common_x1 = max(x1, x2)
    common_p1 = min(p1, p2)
    common_y1 = max(y1, y2)
    common_q1 = min(q1, q2)

    width = common_p1 - common_x1
    height = common_q1 - common_y1

    # 판정 로직
    if width > 0 and height > 0:
        print('a') # 직사각형
    elif width < 0 or height < 0:
        print('d') # 공통부분 없음
    elif width == 0 and height == 0:
        print('c') # 점
    else:
        # width가 0이고 height > 0 이거나, width > 0 이고 height가 0인 경우
        print('b') # 선분