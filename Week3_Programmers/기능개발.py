def solution(progresses, speeds):
    answer = []  # 각 배포마다 몇개의 기능이 배포되는지(날자는 상관X)
    finish = [0] * len(progresses)  # 완료된지 몇일이나 지났는지

    # 뒤에 있는 기능은 앞 기능이 배포될때 함께 배포 #

    while max(finish) != -1:

        # 작업 속도 올려주기
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100 and finish[i] != -1:
                finish[i] += 1

        # 작업 완료된거 answer에 추가하기
        cnt = 0
        for i in range(len(finish)):
            # 완료된 작업이면 건너뛰기
            if finish[i] == -1:
                continue

            if finish[i] == 0:
                break
            else:
                cnt += 1
                finish[i] = -1
        # print(finish)

        if cnt > 0:
            answer.append(cnt)

    return answer