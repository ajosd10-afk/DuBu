import sys
import math

input = sys.stdin.readline

n = int(input().strip()) # 단어 개수 받아오기

reverse_factorial = str(math.factorial(n))[::-1]

count = 0
for i in reverse_factorial:
    if i == '0':
        count += 1
    else:
        break

print(count)