import sys

input = sys.stdin.readline

N = int(input().strip())
dice_num_list = []
max_list = []

for i in range(N):
    input_data = list(map(int, input().strip().split()))
    dice_num_list.append([input_data[0], input_data[-1], input_data[1], input_data[3], input_data[2], input_data[4]])
    
for j in range(1,7):
    target = j
    sub_max_list = []
    for elem in dice_num_list:
        idx = elem.index(target)
        sub_list = elem[:]

        if idx%2 == 0:
            sub_list.pop(idx)
            target = sub_list.pop(idx)
        else:
            sub_list.pop(idx)
            target = sub_list.pop(idx-1)
        
        sub_max_list.append(max(sub_list))

    max_list.append(sum(sub_max_list))
        
result = max(max_list)
print(result)