import sys
from time import time_ns

input = sys.stdin.readline

T = int(input())

user_data = []

for i in range(T):
    age, name = map(str,input().strip().split())
    user_data.append((int(age),name))

user_data = sorted(user_data, key=lambda x: x[0])
# user_data = sorted(user_data, key=lambda x: (list(x.values())[0], list(x.keys())[0]), reverse=False)
for data in user_data:
    print(f'{data[0]} {data[1]}')