import sys

input = sys.stdin.readline

# 1. 입력 받기
w, h = map(int, input().strip().split())
p, q = map(int, input().strip().split())
t = int(input())

# 2. x축 위치 계산
# 개미의 최종 이동 거리는 (현재 위치 + 시간)
# 이것을 왕복 주기(2 * w)로 나눈 나머지가 현재 어디쯤인지를 알려줌
final_x = (p + t) % (2 * w)
if final_x > w:
    # w를 넘어가는 구간은 다시 돌아오는 구간이므로 계산 보정
    final_x = 2 * w - final_x

# 3. y축 위치 계산
# 동일하게 왕복 주기(2 * h)로 계산
final_y = (q + t) % (2 * h)
if final_y > h:
    final_y = 2 * h - final_y

# 4. 결과 출력
print(final_x, final_y)