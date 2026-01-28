T = int(input())

for i in range(1, T+1):
    room_list = []
    h, w, c = map(int,input().split())
    for i in range(1,h+1):
        count_wide = 1
        for o in range(1, w+1):
            if o < 10:
                new_dict = {f'{i}0{o}' : (o-1)+(1/w)}
                room_list.append(new_dict)
            else:
                new_dict = {f'{i}{o}' : (o-1)+(1/w)}
                room_list.append(new_dict)

    sorted_room_list = sorted(room_list, key=lambda d: list(d.values())[0])
    room_number = int(list(sorted_room_list.pop(c-1).keys())[0])
    print(room_number)