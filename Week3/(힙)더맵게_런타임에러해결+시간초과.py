def solution(scoville, K):
    answer = 0

    while min(scoville) < K:
        # 원소 하나인 경우 예외처리
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            else:
                return answer

        scoville.sort()

        new_scoville = scoville[0] + scoville[1] * 2
        del scoville[0:2]
        scoville.append(new_scoville)

        answer += 1

    return answer

