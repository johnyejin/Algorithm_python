def solution(id_list, k):
    answer = 0
    dic = {}

    for i in id_list:
        temp = set(i.split(' '))
        for t in temp:
            dic[t] = dic.get(t, 0) + 1
            if dic[t] <= k:
                answer += 1
        print(dic, answer)

    return answer


# print(solution(["A B C D", "A D", "A B D", "B D"], 2))  # 7
# print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))  # 8
# print(solution(["A A A A A", "A A A A A", "A A"], 2))
print(solution(["A B C D", "A B C D", "A B C D", "A B C D"], 2))