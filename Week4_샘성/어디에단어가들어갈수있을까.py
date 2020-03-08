t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]  # 검정색=0, 흰색=1
    answer = 0

    # 가로부터 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 0:
                if cnt == k:
                    answer += 1
                cnt = 0
                continue
            cnt += 1

        if cnt == k:
            answer += 1

    # 세로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 0:
                if cnt == k:
                    answer += 1
                cnt = 0
                continue
            cnt += 1

        if cnt == k:
            answer += 1

    print("#%d" % (case + 1), answer)