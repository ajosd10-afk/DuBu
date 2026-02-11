import sys

input = sys.stdin.readline

N ,M = map(int, input().strip().split())

name_list = {str(input().strip()): i for i in range(N)}
num_list = {j: k for k, j in name_list.items()}

for i in range(M):
    question = input().strip()

    if not question.isdigit():
        result = name_list[question] + 1
    
    else:
        result = num_list[int(question) - 1]

    print(result)