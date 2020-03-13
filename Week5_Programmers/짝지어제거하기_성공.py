def solution(s):
    answer = 0
    stack = [s[0]]

    for i in range(1, len(s)):
        stack.append(s[i])
        if len(stack) >= 2:
            if stack[len(stack)-1] == stack[len(stack)-2]:
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        answer = 1

    return answer


print(solution('baabaa'))
print(solution('cdcd'))