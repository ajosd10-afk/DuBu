import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())  # 수열의 크기
    stack = []
    result = []
    current = 1  # 스택에 넣을 다음 숫자
    possible = True

    for _ in range(n):
        target = int(input().strip())  # 만들어야 하는 숫자
        
        # 1. target이 나올 때까지 숫자를 push
        while current <= target:
            stack.append(current)
            result.append('+')
            current += 1
            
        # 2. 스택의 top이 target과 일치하는지 확인
        if stack[-1] == target:
            stack.pop()
            result.append('-')
        else:
            # 일치하지 않으면 해당 수열은 만들 수 없음
            possible = False
            break

    # 3. 결과 출력
    if possible:
        print('\n'.join(result))
    else:
        print("NO")

solve()