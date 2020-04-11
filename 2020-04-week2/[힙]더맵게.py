import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K:
        mix = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, mix)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))