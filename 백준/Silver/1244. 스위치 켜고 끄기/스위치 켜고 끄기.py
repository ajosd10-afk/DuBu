import sys

input = sys.stdin.readline

def switch_change(n):

    global switch_list

    if switch_list[n] == 0:
        switch_list[n] = 1
    else:
        switch_list[n] = 0


switch_count = int(input().strip())
switch_list = list(map(int, input().strip().split()))

student_count = int(input().strip())

for i in range(student_count):

    sex, num = map(int, input().strip().split())

    if sex == 1: # 남학생은 자기 배수
        idx = 1 
        while idx*num <= switch_count:
            switch_change(idx*num-1)
            idx += 1


    elif sex == 2: # 여학생은 자기 기준 대칭

        idx = 1
        switch_change(num-1)

        while True:
            if num+idx-1 > switch_count-1 or num-idx-1 < 0:
                break
            if switch_list[num+idx-1] == switch_list[num-idx-1]:
                switch_change(num+idx-1)
                switch_change(num-idx-1)
            else:
                break
            idx += 1

for j in range(0,switch_count, 20):
    print(*(switch_list[j : j+20]))