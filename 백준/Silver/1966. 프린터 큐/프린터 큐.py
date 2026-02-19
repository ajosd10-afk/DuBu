import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스 개수 입력
test_cases = int(input().strip())

for _ in range(test_cases):
    # N: 문서의 개수, M: 궁금한 문서의 현재 위치
    N, M = map(int, input().split())
    
    # 중요도를 입력받아 (중요도, 초기 인덱스) 형태로 큐에 저장
    # 예: 중요도가 [1, 2, 3, 4]라면 [(1, 0), (2, 1), (3, 2), (4, 3)]
    priorities = list(map(int, input().split()))
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    count = 0  # 인쇄된 문서의 수
    
    while queue:
        # 현재 가장 앞에 있는 문서 확인
        current = queue.popleft()
        
        # 큐에 현재 문서보다 중요도가 높은 문서가 하나라도 있는지 확인
        # (current[0]은 중요도)
        if any(current[0] < item[0] for item in queue):
            # 더 높은 게 있다면 가장 뒤로 보냄
            queue.append(current)
        else:
            # 현재 문서가 가장 중요도가 높다면 인쇄
            count += 1
            # 인쇄한 문서가 내가 궁금해하던 위치(M)의 문서인지 확인
            if current[1] == M:
                print(count)
                break