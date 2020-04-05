def solution(road, n):
    damage = []

    # 0 인 구간 찾기
    for i in range(len(road)):
        if road[i] == '0':
            damage.append(i)

    # 가장 긴 도로 찾기
    try:
        # 맨 처음꺼
        answer = damage[n]
        for i in range(1, len(damage) - n):
            temp = damage[i + n] - damage[i - 1] - 1
            if temp > answer:
                answer = temp

        # 맨 마지막꺼
        if len(road) - damage[-n - 1] - 1 > answer:
            answer = len(road) - damage[-n - 1] - 1
    except:
        answer = len(road)

    return answer


# print(solution("111011110011111011111100011111", 3))  # 18
print(solution("001100", 5))  # 6
# print(solution("000", 3))  # 6
