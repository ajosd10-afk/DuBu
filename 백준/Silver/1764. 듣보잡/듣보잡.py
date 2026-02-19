import sys

input = sys.stdin.readline

N , M = map(int, input().strip().split())

no_list = []
result = []

for _ in range(N+M):
    no_list.append(input().strip())
    
no_list = sorted(no_list)
    
for i in range(len(no_list)-1):
    if no_list[i] == no_list[i+1]:
        result.append(no_list[i])

print(len(result))
for elem in result:
    print(elem)