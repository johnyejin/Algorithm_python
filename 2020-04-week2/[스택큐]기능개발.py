def solution(progresses, speeds):
    answer = []
    finish = [0] * len(progresses)

    while max(finish) != -1:

        for i in range(len(speeds)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100 and finish[i] != -1:
                finish[i] += 1

        cnt = 0
        for i in range(len(finish)):
            if finish[i] == -1: continue
            if finish[i] == 0: break

            cnt += 1
            finish[i] = -1
        print(finish)

        if cnt > 0:
            answer.append(cnt)


    return answer


print(solution([93, 30, 55], [1, 30, 5]))