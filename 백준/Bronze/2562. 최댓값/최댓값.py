idx = 1
real_idx = 1

int_1 = int(input())
max = int_1

while True:
    try:
        int_2 = int(input())
        idx += 1
        if max < int_2:
            max = int_2
            real_idx = idx
    except:
        break
    
print(max)
print(real_idx)