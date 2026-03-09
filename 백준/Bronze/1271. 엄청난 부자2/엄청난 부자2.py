import sys

input = sys.stdin.readline

n, m = map(int,input().strip().split())

person = n//m
remain = n%m

print(person)
print(remain)