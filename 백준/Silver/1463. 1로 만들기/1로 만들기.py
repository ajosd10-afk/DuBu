import sys

input = sys.stdin.readline

def simul(now):

    result = []

    for elem in now:

        if elem%2 == 0:
            result.append(elem//2)
        
        if elem%3 == 0:
            result.append(elem//3)

        result.append(elem-1)

        result = list(set(result))

    return result



N = int(input())
now = [N]
count = 0

while True:

    if 1 in now:
        break

    now = simul(now)
    count += 1

print(count)
