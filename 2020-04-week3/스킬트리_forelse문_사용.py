def solution(skill, skill_trees):
    answer = 0

    for t in skill_trees:
        skill_list = list(skill)
        print(skill_list)

        for s in t:
            if s in skill and s != skill_list.pop(0):
                break
        else:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]	))  # 2