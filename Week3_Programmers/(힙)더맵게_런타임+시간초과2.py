def solution(scoville, K):
    answer = 0

    while min(scoville) < K:
        first = min(scoville)
        scoville.pop(scoville.index(first))
        second = min(scoville)
        scoville.pop(scoville.index(second))

        new_scoville = first + second * 2
        scoville.append(new_scoville)

        answer += 1

    if max(scoville) < K:
        return -1

    return answer