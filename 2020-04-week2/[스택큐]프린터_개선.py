from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque()  # [우선순위, 처음위치]

    for i, p in enumerate(priorities):
        dq.append([p, i])

    while len(dq) != 0:
        if dq[0][0] == max(priorities):
            if dq[0][1] == location:
                break

            priorities[dq[0][1]] = 0  # 중요도 0으로 만들기
            dq.popleft()
            answer += 1
        else:
            dq.append(dq[0])
            dq.popleft()

    return answer


# print(solution([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1],0))