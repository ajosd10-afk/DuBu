import sys

input = sys.stdin.readline

N = int(input().strip())
num_count_max = 0

for i in range(N, N//2, -1):
    count = 0
    first_num = N
    second_num = i
    num_list = [N, i]

    while True:
        if True:
            test_num = first_num - second_num
            first_num = second_num
            second_num = test_num

            if test_num < 0:
                break

            else:
                num_list.append(test_num)

    if len(num_list) > num_count_max:
        num_count_max = len(num_list)
        result = num_list

print(num_count_max)
print(*result)
