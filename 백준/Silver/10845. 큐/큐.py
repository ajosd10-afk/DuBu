import sys
from collections import deque

# 입력을 빠르게 받기 위해 readline 사용
input = sys.stdin.readline

# 1. 명령의 수 N 입력 (1 ≤ N ≤ 10,000)
N = int(input())
queue = deque()

for _ in range(N):
    # 명령어를 한 줄씩 읽어서 공백으로 분리
    command = input().split()
    
    # 2. 각 명령어 처리
    if command[0] == 'push':
        queue.append(command[1])
        
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft()) # 맨 앞 요소 제거 및 출력
        else:
            print(-1)
            
    elif command[0] == 'size':
        print(len(queue))
        
    elif command[0] == 'empty':
        print(1 if not queue else 0)
        
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)