num = int(input())
result = 0

for ex in range(1,num+1):
    sum = ex
    for i in str(ex):
        sum += int(i)
    if sum == num:
        result = ex
        break

print(result)