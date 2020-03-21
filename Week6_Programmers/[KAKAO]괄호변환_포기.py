# 균형잡힌 문자열 -> 올바른 문자열
def changeParenthesis(u):
    temp = '(' if u[0] == '(' else ')'
    for i in range(1, len(u) - 1):
        if u[i] == ')':
            temp += '('
        else:
            temp += ')'
    temp += u[-1] if u[-1] == '(' else ')'
    return temp


def solution(p):
    answer = ''
    stack = []  # 올바른 문자열
    reverseStack = []  # 균형잡힌 문자열
    idx = 0
    flag = False

    # 올바른 문자열이면 걍 answer에 붙이고
    # 균형잡힌 문자열이면 u, v로 분리

    for i in range(len(p)):
        if p[i] == '(':
            if len(reverseStack) == 0:
                if flag is True:
                    answer += changeParenthesis(p[idx:i])
                    flag = False
                stack.append('(')
            else:
                reverseStack.pop()
        else:
            if len(stack) == 0:
                answer += p[idx:i]

                if len(reverseStack) == 0:
                    idx = i

                reverseStack.append(')')
                flag = True
            else:
                stack.pop()
        print(answer)

    if idx == 0:
        answer = p
    return answer


# print(solution("(()())()"))  # 그대로
# print(solution(")("))  # "()"
print(solution("()))((()"))  # "()(())()"