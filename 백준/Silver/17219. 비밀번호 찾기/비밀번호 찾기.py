import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split()) # 총 사이트의 수, 찾으려는 사이트 수

password = {}

for _ in range(N):
    
    site, pas = list(map(str, input().strip().split()))
    password[site] = pas

for _ in range(M):
    
    site = str(input().strip())
    print(password[site])
