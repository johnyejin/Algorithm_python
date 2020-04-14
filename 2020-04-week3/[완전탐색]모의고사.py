def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0] * 3

    for idx, a in enumerate(answers):
        if one[idx % 5] == a:
            ans[0] += 1
        if two[idx % 8] == a:
            ans[1] += 1
        if three[idx % 10] == a:
            ans[2] += 1

    maxAns = max(ans)
    for i in range(3):
        if ans[i] == maxAns:
            answer.append(i + 1)

    return answer