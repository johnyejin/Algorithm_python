# 87.5점 (아니 왜 이분탐색보다 느린데 점수가 높지?)
def solution(citations):
    answer = 0

    while True:
        cnt = 0  # h편 이상인 논문 수
        for i in citations:
            if i >= answer:
                cnt += 1
        if cnt == answer:
            break;

        answer += 1

    return answer