import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input()) # case 수 확인

for test in range(1, T+1):

    # 문자열로 입력 받기
    input_data = str(input().strip())
    count_list = defaultdict(int)
    result = None

    if input_data[0] == ')':
        result = 'NO'

    # 각 요소 카운트하기
    for i in input_data:
        if result =='NO':
            break

        if count_list['('] == count_list[')']:
            if i == ')':
                result = 'NO'
                break
        count_list[i] += 1

    if count_list['('] == count_list[')']:
        if result != 'NO':
            result = 'YES'
    else:
        result = 'NO'

    print(result)

