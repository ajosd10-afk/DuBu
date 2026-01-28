from collections import defaultdict

a = int(input())
b = int(input())
c = int(input())

multifly = str(a*b*c)
result = defaultdict(int)

for num in multifly:
    num = int(num)
    result[num] += 1

for i in range(10):
    print(result[i])