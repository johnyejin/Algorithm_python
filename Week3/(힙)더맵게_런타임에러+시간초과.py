def solution(scoville, K):
    answer = 0

    # 매번 정렬 안하려면 min값 2번 찾아서 지워주기

    while min(scoville) < K:
        scoville.sort()

        new_scoville = scoville[0] + scoville[1] * 2
        del scoville[0:2]
        scoville.append(new_scoville)

        answer += 1

    if max(scoville) < K:
        return -1

    return answer

