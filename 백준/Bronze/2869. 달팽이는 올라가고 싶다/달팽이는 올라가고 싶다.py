up_h, down_h, total_h = list(map(int, input().split()))

last_h = total_h - up_h
day_up = up_h - down_h

if last_h % day_up != 0:
    result = last_h // day_up + 2

else:
    result = last_h // day_up + 1
    
print(result)