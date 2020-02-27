from queue import PriorityQueue


def solution(scoville, K):
    answer = 0
    que = PriorityQueue(maxsize=len(scoville))

    for i in scoville:
        que.put(i)

    while True:
        # 길이가 1이 되었을때 예외처리
        if que.qsize() == 1:
            if que.get() < K:
                return -1
            else:
                return answer

        first = que.get()
        second = que.get()
        new_scoville = first + second * 2
        que.put(new_scoville)

        if first >= K:
            break

        answer += 1

    return answer