def solution(progresses, speeds):
    answer = []
    finish = [0] * len(progresses)  # 완료된지 몇일 지났는지 (배포됐으면 -1)

    while max(finish) != -1:

        # 작업 속도 올려주기
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100 and finish[i] != -1:
                finish[i] += 1

        # 배포 가능한게 몇개인지 count
        cnt = 0
        for i in range(len(finish)):
            if finish[i] == -1: continue
            if finish[i] == 0: break

            cnt += 1
            finish[i] = -1
        print(finish)

        # 완료된 작업 answer에 추가
        if cnt > 0:
            answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))