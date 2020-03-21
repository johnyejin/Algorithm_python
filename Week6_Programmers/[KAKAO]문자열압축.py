def solution(s):
    answer = s
    minLen = len(s)

    # 문자열을 1개~len(s)/2개씩 각 단위만큼 잘라서 압축
    for unit in range(1, len(s) // 2 + 1):
        tempAnswer = ""
        temp = s[:unit]
        cnt = 1
        for i in range(unit, len(s), unit):
            # print(i, i+unit, s[i:i+unit])
            if temp == s[i:i+unit]:
                cnt += 1
            else:
                if cnt == 1:
                    tempAnswer += temp
                else:
                    tempAnswer += str(cnt) + temp
                cnt = 1
                temp = s[i:i+unit]

        # 마지막 문자 넣어주기
        if cnt == 1:
            tempAnswer += temp
        else:
            tempAnswer += str(cnt) + temp

        if len(tempAnswer) < minLen:
            answer = tempAnswer
            minLen = len(answer)
        # print(tempAnswer, answer)

    return len(answer)


print(solution("aabbaccc"))  # 7
print()
print(solution("ababcdcdababcdcd"))  # 9
print()
print(solution("abcabcdede"))  # 8
print()
print(solution("abcabcabcabcdededededede"))  # 14
print()
print(solution("xababcdcdababcdcd"))  # 17