def solution(n, building):
    answer = 0  # 밧줄의 최대 길이

    for i in range(n):
        # 왼쪽 탐색
        for a in range(i, 0, -1):
            if building[a] > building[i]:
                if answer <= abs(a - i):
                    answer = abs(a - i)
                break
        # 오른쪽 탐색
        for b in range(i+1, n):
            if building[b] > building[i]:
                if answer <= abs(b - i):
                    answer = abs(b - i)
                break

    return answer


print(solution(10, [8, 4, 7, 8, 10, 2, 9, 7, 8, 12]))