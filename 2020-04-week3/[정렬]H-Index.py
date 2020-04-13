def solution(citations):
    length = len(citations)
    citations.sort()

    for idx, c in enumerate(citations):
        # 논문이 인용된 횟수 >= 인용된 논문의 개수
        if c >= length - idx:
            return length - idx

    return 0


print(solution([3, 0, 6, 1, 5]))