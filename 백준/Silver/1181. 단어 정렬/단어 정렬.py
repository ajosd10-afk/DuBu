import sys

input = sys.stdin.readline

n = int(input().strip()) # 단어 개수 받아오기

input_list = [] # 입력된 값을 받을 빈 리스트
for j in range(n):
    input_list.append(str(input().strip())) # 입력된 단어 리스트

input_list = list(set(input_list))
sorted_list = sorted(input_list, key=lambda x: (len(x),x)) # 길이와 사전순으로 정렬

for i in sorted_list: # 하나씩 뽑아와서 프린트
    print(i)