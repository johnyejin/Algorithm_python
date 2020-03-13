from itertools import permutations


# 순열 구하면 각 원소들이 tuple 형태로 나오는데 list로 바꿀수 있는 방법이 없을까...
def solution(numbers):
    answer = ''
    permutation_list = permutations(numbers)
    max_number = 0

    for i in permutation_list:
        temp = int(''.join(map(str, i)))

        if max_number < temp:
            max_number = temp

    answer = str(max_number)
    return answer