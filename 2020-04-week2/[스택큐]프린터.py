from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque()
    pri = deque()

    for i, p in enumerate(priorities):
        dq.append([p, i])
        pri.append(p)


    while len(dq) != 0:
        if dq[0][0] == max(pri):
            if dq[0][1] == location:
                # dq.popleft()
                break
            dq.popleft()
            pri.popleft()
        else:
            dq.append(dq[0])
            dq.popleft()
            pri.append(pri[0])
            pri.popleft()
        print(dq, pri)

    return len(priorities) - len(dq) + 1


# print(solution([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1],0))