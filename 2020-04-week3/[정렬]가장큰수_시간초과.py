from itertools import permutations


def solution(numbers):
    per = list(permutations(numbers, len(numbers)))
    perlist = []
    numbers = list(map(str, numbers))
    numbers.sort()
    print(numbers)

    for p in per:
        temp = "".join(map(str, p))
        perlist.append(temp)

    return max(perlist)


# print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330