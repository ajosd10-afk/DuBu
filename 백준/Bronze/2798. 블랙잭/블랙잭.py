card_num, target = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0

if card_num == 3:
    result = card_list[0] + card_list[1] + card_list[2]

else:
    for i in range(card_num):
        for j in range(card_num):
            for k in range(card_num):
                if i != j and j != k and k != i:
                    card_sum = card_list[i] + card_list[j] + card_list[k]
                    if card_sum > target:
                        card_sum = None
                else:
                    card_sum = None
                    
                if card_sum == None:
                    pass
                elif (target - card_sum) < (target - result):
                    result = card_sum

print(result)