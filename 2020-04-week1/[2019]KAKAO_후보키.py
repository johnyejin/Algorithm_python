from itertools import *


def checkMinimality(candidate, target):
    for i in range(len(candidate)):
        cnt = 0
        for j in range(len(candidate[i])):
            if candidate[i][j] in target:
                cnt += 1
        if cnt == len(candidate[i]):
            return False

    return True


def checkUniqueness(relation, combi):
    arr = []
    for i in range(len(relation)):
        temp = []
        for j in range(len(combi)):
            temp.append(relation[i][combi[j]])

        if temp in arr:
            return False

        arr.append(temp)
        # print(arr)

    return True


def solution(relation):
    answer = 0
    combiList = [i for i in range(len(relation[0]))]
    combination = []
    candidate = []

    for i in range(1, len(relation[0])+1):
        combination.append(list(combinations(combiList, i)))
    print(combination)

    for i in range(len(combination)):
        for j in range(len(combination[i])):
            # print("유일성", checkUniqueness(relation, list(combination[i][j])))
            # print("최소성", checkMinimality(candidate, combination[i][j]))

            if checkUniqueness(relation, combination[i][j]) and checkMinimality(candidate, combination[i][j]):
                answer += 1
                candidate.append(list(combination[i][j]))
                # print("후보키", candidate)

    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))