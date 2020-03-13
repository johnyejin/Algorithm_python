def solution(s):
    answer = 1
    idx = 0

    while len(s) != 0:
        if idx == len(s) - 1:
            answer = 0
            break

        if s[idx] == s[idx+1]:
            s = s[:idx] + s[idx+2:]
            idx = 0
            continue

        idx += 1
        print(s)

    return answer


print(solution('baabaa'))
print(solution('cdcd'))