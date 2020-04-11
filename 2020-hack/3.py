import math

def solution(n, m, k):
    answer = 0

    if n > m or (n == m and k > 1):
        return answer

    answer = (math.factorial(m-1) // (math.factorial(m-n) * math.factorial(n-1)) - (math.factorial(n) // (math.factorial(m-n-k) * math.factorial(2*n-m+k))) * n) // 2

    return answer


# print(solution(3, 8, 4))
print(solution(50, 150, 20))