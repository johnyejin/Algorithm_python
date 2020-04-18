def dfs(numbers, target, total, cnt):
    global answer

    if cnt == len(numbers):
        if total == target:
            answer += 1
        return

    dfs(numbers, target, total + numbers[cnt], cnt + 1)
    dfs(numbers, target, total - numbers[cnt], cnt + 1)


def solution(numbers, target):
    global answer

    dfs(numbers, target, 0, 0)

    return answer


answer = 0
print(solution([1,1,1,1,1], 3))