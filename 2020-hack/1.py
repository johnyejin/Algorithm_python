def check(end, target, delivery, result):
    for i in range(end):
        if delivery[i][2] == 0:
            if delivery[i][0] == target:
                result[delivery[i][1]] = 2
            if delivery[i][1] == target:
                result[delivery[i][0]] = 2
    return result


def solution(n, delivery):
    answer = ''
    result = [0] * (n + 1)  # 확실하게 남아있으면 -1, 모르면 0 또는 1, 없으면 2

    for i in range(len(delivery)):
        if delivery[i][2] == 1:
            result[delivery[i][0]] = -1
            result[delivery[i][1]] = -1
            # 이전 주문 체크
            result = check(i, delivery[i][0], delivery, result)
            result = check(i, delivery[i][1], delivery, result)
        else:
            if result[delivery[i][0]] == -1:
                result[delivery[i][1]] = 2
            elif result[delivery[i][1]] == -1:
                result[delivery[i][0]] = 2

    for i in range(1, n+1):
        if result[i] is -1:
            answer += 'O'
        elif result[i] is 2:
            answer += 'X'
        else:
            answer += '?'

    return answer


# print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))  # "O?O?X?"
# print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))  # "O?O?XXO"
print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[4, 7, 0],[3,2,0],[7,6,0],[3,7,1],[2,5,0]]))  # "OXOXXXO"