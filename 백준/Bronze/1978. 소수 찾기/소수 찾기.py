N = int(input())

num_list = list(map(int,input().split()))
count_result = 0

for num in num_list:
    point = '소수'
    if num > 2:
        for n in range(2,num):
            if num % n == 0:
                point = '짝수'
                break
        if point == '소수':
            count_result += 1
    
    elif num == 2:
        count_result += 1
        
print(count_result)