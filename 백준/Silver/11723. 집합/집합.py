import sys

# 빠른 입출력 필수
input = sys.stdin.readline
print = sys.stdout.write

# 연산의 수 입력
M = int(input().strip())

# 공집합 S (정수 1개로 메모리 압축)
S = 0

for _ in range(M):
    query = input().split()
    cmd = query[0]
    
    # 명령어에 따라 비트 연산 수행
    if cmd == "add":
        x = int(query[1])
        S |= (1 << x)  # x번째 비트를 1로 켬 (OR 연산)
        
    elif cmd == "remove":
        x = int(query[1])
        S &= ~(1 << x) # x번째 비트만 0으로 끔 (AND NOT 연산)
        
    elif cmd == "check":
        x = int(query[1])
        if S & (1 << x): # x번째 비트가 1인지 확인 (AND 연산)
            print("1\n")
        else:
            print("0\n")
            
    elif cmd == "toggle":
        x = int(query[1])
        S ^= (1 << x)  # x번째 비트의 상태를 뒤집음 (XOR 연산)
        
    elif cmd == "all":
        # 1부터 20까지의 비트를 모두 1로 만듦
        # (1 << 21)은 10000...0 이고, 여기서 1을 빼면 01111...1 이 됨
        S = (1 << 21) - 1 
        
    elif cmd == "empty":
        # 모든 비트를 0으로 만듦
        S = 0