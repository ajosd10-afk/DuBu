import sys

input = sys.stdin.readline

trans_dict = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}

n = input().strip()

result = 0

for i in range(len(n)):
    elem = trans_dict[n[-(i+1)]]
    result += (16**i)*elem

print(result)