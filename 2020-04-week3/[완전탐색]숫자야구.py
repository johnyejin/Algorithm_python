def solution(baseball):
    answer = 0

    for num in range(123, 988):
        a, b, c = str(num)[0], str(num)[1], str(num)[2]
        cnt = 0
        if a == b or b == c or a == c: continue

        for i in range(len(baseball)):
            A, B, C = str(baseball[i][0])[0], str(baseball[i][0])[1], str(baseball[i][0])[2]
            strike, ball = 0, 0

            if a == A: strike += 1
            if b == B: strike += 1
            if c == C: strike += 1

            if a == B or a == C: ball += 1
            if b == A or b == C: ball += 1
            if c == A or c == B: ball += 1

            if strike == baseball[i][1] and ball == baseball[i][2]: cnt += 1

        if cnt == len(baseball):
            answer += 1

    return answer


print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))  # 2