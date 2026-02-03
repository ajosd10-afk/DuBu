import sys

input = sys.stdin.readline

n = int(input()) # 인원 받기

user_data = []

for _ in range(n):
    wei, hei = map(int,input().strip().split())
    user_data.append((wei, hei))

rank = []

for data in user_data:
    count = 1
    wei, hei = data
    for other in user_data:
        o_wei, o_hei = other
        if data == other:
            pass
        elif o_wei > wei and o_hei > hei:
            count += 1
    rank += [count]

for r in rank:
        print(r, end=' ')
