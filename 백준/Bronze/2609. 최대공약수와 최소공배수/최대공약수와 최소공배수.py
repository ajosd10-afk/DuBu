def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return (a * b) // get_gcd(a, b)

# 예시
num1, num2 = sorted(list(map(int, input().split())))

print(get_gcd(num1, num2))
print(get_lcm(num1, num2))
    