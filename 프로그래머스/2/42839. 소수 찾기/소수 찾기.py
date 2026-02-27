import itertools

def solution(numbers):
    
    elem_list = [x for x in numbers]
    maked_num_list = []
    max_num = -100

    for count in range(1,len(elem_list)+1):
        sub_num = itertools.permutations(elem_list,count)
        for elem in sub_num:
            int_num = int(''.join(elem))
            if max_num < int_num:
                max_num = int_num
            maked_num_list.append(int_num)
    
    maked_num_list = set(maked_num_list)

    num_list = [True]*(max_num+1)
    num_list[0], num_list[1] = False, False

    for i in range(2, (max_num//2+1)):

        if num_list[i] == True:
            for j in range(2*i,len(num_list),i):
                num_list[j] = False

    count = 0

    for i in maked_num_list:
        if num_list[i] == True:
            count += 1
    
    return count