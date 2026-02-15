import sys

input = sys.stdin.readline

W, H = map(int, input().strip().split())

N = int(input())

wide_list = [0]
height_list = [0]

for i in range(N):

    key, num = map(int, input().strip().split())

    if key == 0:
        height_list.append(num)
    
    elif key == 1:
        wide_list.append(num)

wide_list.append(W)
height_list.append(H)

wide_list = sorted(wide_list)
height_list = sorted(height_list)

wide_max = 0
height_max = 0

for i in range(len(wide_list)-1 ,0,-1):
    wide_max = wide_list[i] - wide_list[i-1] if wide_list[i] - wide_list[i-1] > wide_max else wide_max

for i in range(len(height_list)-1, 0, -1):
    height_max = height_list[i] - height_list[i-1] if height_list[i] - height_list[i-1] > height_max else height_max

print(wide_max*height_max)    