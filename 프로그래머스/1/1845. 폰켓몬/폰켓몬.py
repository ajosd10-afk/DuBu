def solution(nums):
    answer = 0
    num_list = []
    
    # 일단 서로 다른 포켓몬의 수를 카운트
    # 카운트 값이 중간값 이상이면 그냥 중간값 반환
    # 중간값보다 작으면 그냥 반환
    for num in nums:
        if num not in num_list:
            num_list.append(num)
            answer += 1
        else:
            pass
    
    if answer <= len(nums)/2:
        pass
    else:
        answer = len(nums)/2
    
    return answer