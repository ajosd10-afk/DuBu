N = int(input())

t_shirt_list = list(map(int,input().split()))
t, p = map(int,input().split())

shirt_pack = 0

for shirt in t_shirt_list:
    if shirt % t == 0:
        shirt_pack += shirt // t
    elif shirt % t != 0:
        shirt_pack += (shirt // t) + 1
    
print(shirt_pack)
print(N//p, end = ' ')
print(N%p)