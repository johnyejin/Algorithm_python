import collections


def solution(clothes):
    answer = 1
    kind = []

    for a, b in clothes:
        kind.append(b)

    kind = collections.Counter(kind)

    for i in kind.values():
        answer *= (i + 1)

    return answer - 1