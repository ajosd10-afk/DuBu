import sys

isbn = input()

target_idx = isbn.find('*')

final_result = 0
result = 0
idx = 0

if target_idx == 12:
    for i in isbn[:12]:
        if idx % 2 == 0:
            result += int(i)
        else:
            result += 3*int(i)
        idx += 1
else:
    for i in isbn:
        if idx == target_idx:
            pass
        else:
            if idx % 2 == 0:
                result += int(i)
            else:
                result += 3*int(i) 
        idx += 1


if target_idx % 2 == 0:
    for i in range(1,10):
        if (result + i) % 10 == 0:
            final_result = i
            break
else:
    for i in range(1,10):
        if (result + i*3) % 10 == 0:
            final_result = i
            break           

print(final_result)