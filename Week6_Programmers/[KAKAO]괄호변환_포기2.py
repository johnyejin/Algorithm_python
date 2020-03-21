# 균형잡힌 문자열 -> 올바른 문자열
def changeParenthesis(u):
    temp = '(' if u[0] == ')' else ')'
    for i in range(1, len(u) - 1):
        if u[i] == ')':
            temp += '('
        else:
            temp += ')'
    temp += ')' if u[-1] == '(' else '('
    return temp


def solution(p):
    answer = ''
    stack = []
    reverseStack = []
    flag = False  # True면 균형잡힌, False면 올바른
    cnt = 0

    for i in range(len(p)):
        if p[i] == '(':
            if len(reverseStack) != 0:
                reverseStack.pop()
            else:
                # 균형잡힌 괄호가 나오다가 올바른 괄호가 나온 경우
                if flag is True:
                    answer += changeParenthesis(p[len(answer) - 1:len(answer) - 1 + cnt * 2])
                    cnt = 0
                    flag = False
                stack.append('(')
        else:
            # 올바른 괄호 -> 균형잡힌 괄호가 나온 경우
            if len(stack) == 0:
                if len(answer) == 0:
                    answer += p[:i]
                else:
                    answer += p[len(answer) - 1:len(answer) - 1 + i]
                flag = True
                cnt += 1
                reverseStack.append(')')
            else:
                stack.pop()
        print(answer, flag, stack, reverseStack)


        # 마지막 문자인 경우
        if i == len(p) - 1:
            if flag is True:
                if len(answer) == 0:
                    answer += changeParenthesis(p)
                else:
                    answer += changeParenthesis(p[len(answer) - 1:])
            else:
                answer += p[len(answer) - 1:]

    return answer


# print(solution("(()())()"))  # 그대로
# print(solution(")("))  # "()"
print(solution("()))((()"))  # "()(())()"