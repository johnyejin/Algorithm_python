def solution(skill, skill_trees):
    answer = 0
    dic = dict()

    for i in range(len(skill)):
        dic[skill[i]] = i
    print(dic)

    for i in range(len(skill_trees)):
        check = [-1]
        flag = True
        for j in range(len(skill_trees[i])):
            # 스킬순서에 있는거면
            if skill_trees[i][j] in dic:
                if check[len(check)-1] + 1 != dic[skill_trees[i][j]]:
                    flag = False
                    break
                check.append(dic[skill_trees[i][j]])

        if flag: answer += 1
        print(check)

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]	))  # 2