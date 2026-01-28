N = int(input())

num_list = list(map(int,input().split()))
sort_num = sorted(num_list)
print(f'{sort_num[0]}', end=' ')
print(f'{sort_num[-1]}')