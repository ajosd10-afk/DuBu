h, m = map(int,input().split())
minutes = h*60 + m
minutes -= 45
if minutes < 0:
    minutes += 24*60
h = minutes // 60
m = minutes % 60
print(h, end=" ")
print(m)