import sys

input = sys.stdin.readline

while True:

    n = int(input().strip())

    if n == 0:
        break

    for i in range(1,n+1):

        print('*'*i)