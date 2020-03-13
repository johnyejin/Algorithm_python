from itertools import permutations


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    permutation_list = []
    permutation_unique = set()

    for i in range(len(numbers)):
        permutation_list.append(list(map(''.join, permutations(numbers, i + 1))))

    for i in range(len(permutation_list)):
        for j in permutation_list[i]:
            permutation_unique.add(int(j))

    for i in permutation_unique:
        if isPrime(i):
            answer += 1

    return answer