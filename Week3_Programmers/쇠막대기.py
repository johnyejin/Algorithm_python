def solution(arrangement):
    answer = 0
    stack = []

    # ()일때만 레이저

    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            # 레이저인 경우
            if arrangement[i - 1] == '(':
                answer += len(stack)
            else:  # 막대기가 끊긴 경우
                answer += 1

    return answer