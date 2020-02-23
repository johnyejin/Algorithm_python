def solution(citations):
    answer = 0
    left, right = 0, len(citations) - 1

    while True:
        mid = (left + right) // 2
        cnt = 0
        for i in citations:
            if i > mid:
                cnt += 1

        if cnt == len(citations):
            return cnt

        if cnt == mid:
            answer = mid
            break
        elif cnt > mid:
            left = mid + 1
        else:
            right = mid - 1

    return answer