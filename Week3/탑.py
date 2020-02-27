def solution(heights):
    answer = [0] * len(heights)

    # 모든 탑은 동시에 '왼쪽'으로 신호를 보냄
    # 자신보다 높은 탑에서만 수신 가능

    for i in range(len(heights) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if heights[j] > heights[i]:
                answer[i] = j + 1
                break

    return answer