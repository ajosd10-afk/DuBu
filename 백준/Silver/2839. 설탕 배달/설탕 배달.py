import sys

input = sys.stdin.readline

N = int(input())

count_5 = 0
count_3 = 0

for i in range(1, (N//3)+1):
    total = N

    if total % 5 == 0:
        count_5 = total / 5
        break

    if (N - 3*i) % 5 == 0:
        count_3 = i
        count_5 = (N - 3*i) / 5
        break
    
    elif i == (N//3):
        count_5 = -1

result = int(count_5 + count_3)

print(f'{result}')