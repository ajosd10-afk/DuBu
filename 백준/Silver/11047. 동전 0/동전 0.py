import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int,input().strip().split())

coin_data = ([int(input().strip()) for _ in range(N)])

coin_cnt = 0

for i in range(N-1,-1,-1):

    target = coin_data[i]

    if K == 0:
        break

    while K >= target:
        K -= target
        coin_cnt += 1

print(f'{coin_cnt}\n')