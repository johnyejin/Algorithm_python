def solution(s):
    answer = ''
    string_list = []

    # 짝수번째 알파벳 - 대문자 / 홀수번재 알파벳 - 소문자
    # (단어를 기준으로 짝홀수 판별)

    for i in range(len(s)):
        string_list.append(s[i])

    cnt = 0
    for i in range(len(s)):
        if string_list[i] == ' ':
            answer += ' '
            cnt = 0
            continue

        if cnt % 2 == 0:
            answer += str(string_list[i]).upper()
        else:
            answer += str(string_list[i]).lower()
        cnt += 1

    return answer