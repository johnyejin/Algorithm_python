def solution(string):
    answer = ""
    name = []
    cnt = []

    # 원소는 대문자로 구분
    for i in range(len(string)):
        if string[i].isdigit():  # 숫자인 경우
            # 원소의 개수가 10인 경우
            if string[i] == '0':
                cnt.pop()
                cnt.append('10')
            else:
                cnt.append(string[i])
        else:  # 문자인 경우
            # 소문자인 경우
            if string[i].islower():
                name.pop()
                name.append(string[i-1:i+1])
            else:
                name.append(string[i])

    print(name, cnt)

    # 원소 & 원소의 개수가 맞지 않으면 걍 error 리턴
    if len(name) != len(cnt):
        return "error"

    for n, c in zip(name, cnt):
        if c == '1':
            answer += n
        else:
            answer += n
            answer += c

    return answer


print(solution("HO21"))
# print(solution("CO12"))
# print(solution("HSO2110"))
# print(solution("NaCl1"))