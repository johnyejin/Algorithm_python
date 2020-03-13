from collections import deque


def solution(priorities, location):
    answer = 1
    dq = deque()  # [우선순위, 처음 위치]

    for i in range(len(priorities)):
        dq.append([priorities[i], i])

    while len(dq) != 0:
        if max(priorities) > dq[0][0]:
            dq.append(dq[0])
            dq.popleft()
        else:
            if location == dq[0][1]:
                return answer

            priorities[dq[0][1]] = 0  # 한개 뺐으면 그 우선순위는 0으로 초기화시켜주기
            dq.popleft()
            answer += 1

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))