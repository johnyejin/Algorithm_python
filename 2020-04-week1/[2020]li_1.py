def solution(inputString):
    answer = 0  # 총 괄호 쌍의 수
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []

    for i in range(len(inputString)):
        if inputString[i] == '(':
            stack1.append('(')
        elif inputString[i] == ')':
            if len(stack1) == 0: return -1
            stack1.pop()
            answer += 1

        elif inputString[i] == '{':
            stack2.append('{')
        elif inputString[i] == '}':
            if len(stack2) == 0: return -1
            stack2.pop()
            answer += 1

        elif inputString[i] == '[':
            stack3.append('[')
        elif inputString[i] == ']':
            if len(stack3) == 0: return -1
            stack3.pop()
            answer += 1

        elif inputString[i] == '<':
            stack4.append('<')
        elif inputString[i] == '>':
            if len(stack4) == 0: return -1
            stack4.pop()
            answer += 1

    return answer