import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:

        # 예외처리
        if len(heap) == 1:
            if heap[0] < K:
                return -1

        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)

        answer += 1

    return answer