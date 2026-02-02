import sys

n = int(sys.stdin.readline())

num_list = [0]*10000
for i in range(n):
    num = int(sys.stdin.readline())
    num_list[num-1] += 1

idx = 0
for j in num_list:
    if j != 0:
        for k in range(j):
            print(idx+1)
    idx += 1
