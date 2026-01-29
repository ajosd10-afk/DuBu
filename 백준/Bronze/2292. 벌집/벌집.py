# 입력 받기
n = int(input())

# 초기 설정
# room_edge: 해당 겹의 가장 큰 방 번호
# layer: 지나는 방의 개수 (1번 방부터 시작하므로 1)
room_edge = 1
layer = 1

# 입력받은 n이 현재 겹의 최대 번호보다 클 때까지 반복
while n > room_edge:
    # 다음 겹의 최대 번호는 현재 최대 번호 + (6 * 현재 layer)
    room_edge += 6 * layer
    # 한 겹 밖으로 나갔으므로 1 증가
    layer += 1

print(layer)