from itertools import permutations


def isPrime(x):
    if x == 0 or x == 1: return False
    if x == 2: return True
    for i in range(2, x // 2 + 1):
        if x % i == 0: return False
    return True


def solution(numbers):
    answer = 0
    per = []
    unique = set()

    for i in range(1, len(numbers) + 1):
        per.append(list(map(''.join, permutations(numbers, i))))

    for i in range(len(per)):
        for j in range(len(per[i])):
            unique.add(int(per[i][j]))

    for u in unique:
        if isPrime(u):
            answer += 1

    return answer