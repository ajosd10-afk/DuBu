N = int(input())
d = 1
s = 1
for i in range(1, N+1):
    print(f"{' '*(N-d)}{'*'*s}")
    d += 1
    s += 1