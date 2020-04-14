import math

def divisor(num):
    arr = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            arr.append([i, num // i])
    return arr

def solution(brown, red):
    divide = divisor(red)
    print(divide)

    for idx, (a, b) in enumerate(divide):
        if (a + b + 2) * 2 == brown:
            return [b+2, a+2]


print(solution(24, 24))