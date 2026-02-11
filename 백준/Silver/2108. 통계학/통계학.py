import sys
from collections import Counter

# 입력을 빠르게 받기 위해 readline 사용
input = sys.stdin.readline

# 일반적인 사사오입 반올림 함수 정의
def my_round(n):
    return int(n + 0.5) if n >= 0 else int(n - 0.5)

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort() # 중앙값과 범위를 위해 정렬

# 1. 산술평균
print(my_round(sum(nums) / N))

# 2. 중앙값
print(nums[N // 2])

# 3. 최빈값
cnt = Counter(nums).most_common() # (값, 빈도수) 형태의 리스트 반환
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    # 최빈값이 여러 개인 경우 두 번째로 작은 값 출력
    print(cnt[1][0])
else:
    # 최빈값이 하나인 경우
    print(cnt[0][0])

# 4. 범위
print(nums[-1] - nums[0])