import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# deque로 생성
queue = deque(range(1, n + 1)) 

while len(queue) > 1:
   
    queue.popleft() # 제일 위에 있는 카드를 바닥에 버린다.
    
   
    # (맨 앞을 뽑아서 -> 맨 뒤에 붙임)
    queue.append(queue.popleft()) # 제일 위에 있는 카드를 제일 아래로 옮긴다.

# 마지막 남은 카드 출력
print(queue[0])