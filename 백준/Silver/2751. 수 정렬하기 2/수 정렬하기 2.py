import sys

input = sys.stdin.readline

n = int(input().strip())

num_list = []
for i in range(n):
    num = int(input().strip())
    num_list.append(num)

sort_list = sorted(list(set(num_list)), reverse=False)

for j in sort_list:
    print(j)