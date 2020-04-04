def solution(N, stages):
    fail = [[0, idx] for idx in range(N + 1)]  # [실패율, 스테이지 번호]
    stages.sort()

    temp = stages[0]
    cnt = 1
    for i in range(1, len(stages)):
        if temp != stages[i]:
            print(cnt, len(stages) - i + cnt, "~", temp)
            fail[temp] = [cnt / (len(stages) - i + cnt), temp]
            temp = stages[i]
            cnt = 1
        else:
            cnt += 1
        print(fail)

    # 맨 마지막꺼 추가
    if cnt != 1 and temp <= N:
        fail[temp] = [cnt / (len(stages) - i - 1 + cnt), temp]
    print(fail)

    fail.pop(0)  # idx=0 인거 지워버리기
    fail = sorted(fail, key=lambda x: -x[0])

    answer = [f[1] for f in fail]
    return answer


# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))