import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

station_list = list(map(int,input().strip().split()))

check_dict = {} # 연결된 역 찾기
count = 0
result = []

for elem in range(len(station_list)):
    check_dict[station_list[elem]] = [station_list[(elem - 1)%len(station_list)], station_list[(elem + 1)%len(station_list)]]
    count += 1
    
for _ in range(M):
    
    trigger, *args = map(str, input().strip().split())
    
    if trigger == 'BN':
        i, j = [*args]
        i = int(i)
        j = int(j)
        after_station = check_dict[i][1]
        check_dict[j] = [i, after_station]
        check_dict[i][1] = j
        check_dict[after_station][0] = j
        result.append(after_station)
        count += 1
        
    elif trigger == 'BP':
        i, j = [*args]
        i = int(i)
        j = int(j)
        before_station = check_dict[i][0]
        check_dict[j] = [before_station, i]
        check_dict[i][0] = j
        check_dict[before_station][1] = j
        result.append(before_station)
        count += 1
        
    elif trigger == 'CN':
        i = [*args][0]
        i = int(i)
        after_station = check_dict[i][1]
        two_after_station = check_dict[after_station][1]
        if count >= 2:
            check_dict[i][1] = two_after_station
            check_dict[two_after_station][0] = i
            del check_dict[after_station]
            count -= 1
            result.append(after_station)
            
    
    elif trigger == 'CP':
        i = [*args][0]
        i = int(i)
        before_station = check_dict[i][0]
        two_before_station = check_dict[before_station][0]
        if count >= 2:
            check_dict[i][0] = two_before_station
            check_dict[two_before_station][1] = i
            del check_dict[before_station]
            count -= 1
            result.append(before_station)

        
print('\n'.join(map(str,result)))

# 2 7 6 3 5 11
