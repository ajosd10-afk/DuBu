while True:
    n = int(input())
    if n == -1:
        break
    
    divisor_lst = []
    for i in range(1, n):
        if n % i == 0:
            divisor_lst.append(i)
            
    if sum(divisor_lst) == n:
        joined_str = ' + '.join(map(str, divisor_lst))
        print(f"{n} = {joined_str}")
    else:
        print(f"{n} is NOT perfect.")