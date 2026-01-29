# 0이 앞에 올 수 없다.
while True:
    try:
        num = input()
        new_num = num[::-1]
        if num == '0':
            break
        else:
            if num == new_num:
                result = 'yes'
            else:
                result = 'no'
        print(result)
    except:
        break