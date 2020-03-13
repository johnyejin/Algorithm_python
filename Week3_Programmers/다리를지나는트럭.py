from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    dq = deque()  # [트럭무게, 다리를 지난 시간]
    dq.append([truck_weights[0], bridge_length])
    truck_weights.pop(0)

    while len(dq) != 0 and dq[0][1] != 0:
        temp = 0  # 다리를 다 건넌 트럭
        total_weight = 0  # 현재 다리에 있는 트럭들의 총 무게

        # dq에 있는 트럭들의 시간 -1
        for i in range(len(dq)):
            total_weight += dq[i][0]
            dq[i][1] -= 1
            if dq[i][1] == 0:
                temp += 1

        # 다리를 다 건넌 트럭만큼 지우기
        for i in range(temp):
            total_weight -= dq[i][0]
            dq.popleft()

        # (현재 다리에 있는 트럭들 무게 + 대기트럭)이 다리 무게보다 작으면 다리에 추가!
        if len(truck_weights) != 0 and total_weight + truck_weights[0] <= weight:
            dq.append([truck_weights[0], bridge_length])
            truck_weights.pop(0)

        answer += 1

        print(answer, dq, truck_weights)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print()
print(solution(100, 10, [10]))
print()
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))