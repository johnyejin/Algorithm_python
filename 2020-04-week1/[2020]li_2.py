from itertools import combinations


def check(answer_sheet, one, two):
    suspicion = 0  # 의심문항
    continuous = 1  # 가장 긴 연속된 의심문항 수

    idx = -1
    cnt = 0
    for i in range(len(answer_sheet)):
        if one[i] == two[i] and one[i] != answer_sheet[i]:
            suspicion += 1
            if idx + 1 == i:
                cnt += 1
                idx += 1
            else:
                if cnt > continuous:
                    continuous = cnt
                cnt = 0

    if suspicion == 0:
        return 0, 0
    return suspicion, continuous


def solution(answer_sheet, sheets):
    answer = -1  # 가장 높은 부정행위 가능성 지수
    c = [i for i in range(len(sheets))]
    combination = list(combinations(c, 2))  # 가능한 모든 조합
    suspicion = 0  # 의심문항
    continuous = 0  # 가장 긴 연속된 의심문항 수

    # 같은 선택지인데 오답인 문항 찾기
    for c in combination:
        suspicion, continuous = check(answer_sheet, sheets[c[0]], sheets[c[1]])
        # print(suspicion, continuous)
        temp = suspicion + continuous ** 2
        if temp > answer:
            answer = temp

    return answer