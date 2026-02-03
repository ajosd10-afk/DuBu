import sys
input = sys.stdin.readline

# 1. 14층 14호까지 담을 수 있는 15x15 크기의 2차원 리스트 생성 (0으로 초기화)
# k, n 제한이 14까지이므로 인덱스를 편하게 쓰기 위해 15로 잡습니다.
apt = [[0] * 15 for _ in range(15)]

# 2. 0층 초기화 (0층 i호에는 i명이 산다)
for i in range(1, 15):
    apt[0][i] = i

# 3. 전체 아파트 인원수 미리 채우기 (Bottom-Up)
# 1층부터 14층까지
for k in range(1, 15):
    for n in range(1, 15):
        # 공식: k층 n호 = (k층 n-1호) + (k-1층 n호)
        # 설명: 내 옆집(같은 층 이전 호수)까지의 합에 + 내 아랫집 사람 수
        # 이렇게 하면 매번 sum()을 쓰지 않아도 누적 합이 됩니다.
        apt[k][n] = apt[k][n-1] + apt[k-1][n]

# 4. 테스트 케이스 입력받고 정답 바로 출력
t = int(input().strip())

for _ in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n])  # 미리 계산된 값 출력 (O(1))