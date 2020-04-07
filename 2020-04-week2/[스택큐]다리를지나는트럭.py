def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = len(truck_weights)  # 트럭 개수
    after = []  # 다리를 지난 트럭
    ing = []
    rest = []
    # ing = [truck_weights[0]]  # 다리를 건너는 트럭
    # rest = [bridge_length - 1]  # 다리를 건너는 트럭들의 남은 시간
    # truck_weights.pop(0)

    while len(after) != cnt:
        for i in range(len(ing)):
            rest[i] -= 1

        if len(rest) != 0 and rest[0] < 0:
            after.append(ing[0])
            ing.pop(0)
            rest.pop(0)

        if len(truck_weights) != 0 and sum(ing) + truck_weights[0] <= weight and len(ing) < bridge_length:
            ing.append(truck_weights[0])
            rest.append(bridge_length - 1)
            truck_weights.pop(0)



        answer += 1
        print(after, ing, rest, truck_weights, answer)

    return answer


# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))