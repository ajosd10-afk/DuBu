import sys

a = sys.stdin.readline()
b = sys.stdin.readline()
c = sys.stdin.readline()
list = [a, b, c]
num_idx = 0
num = 0
idx = 0
for i in list:
    try:
        num = int(i)
        num_idx = idx
        idx += 1
    except ValueError:
        idx += 1
        pass

final_num = num + (3-num_idx)

if final_num % 3 == 0 and final_num % 5 == 0:
    print('FizzBuzz')
elif final_num % 3 == 0 and final_num % 5 != 0:
    print('Fizz')
elif final_num % 3 != 0 and final_num % 5 == 0:
    print('Buzz')
else:
    print(final_num)