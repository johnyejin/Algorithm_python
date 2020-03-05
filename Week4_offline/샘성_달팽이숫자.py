t = int(input())

for a in range(t):
    n = int(input())
    direction = 0  # Right=0 Down=1 Left=2 Up=3
    right, down, left, up = 0, n-1, n-1, 0
    row, column = 0, 0
    arr = [[0]*n for _ in range(n)]
    num = 1

    while num <= n ** 2:

        if direction is 0:  # 오른쪽
            if right >= n: continue
            for i in range(n):
                if arr[right][i] != 0:
                    continue
                arr[right][i] = num
                num += 1
            right += 1
            direction = 1
        elif direction is 1:  # 아래
            if down >= n: continue
            for i in range(n):
                if arr[i][down] != 0:
                    continue
                arr[i][down] = num
                num += 1
            down -= 1
            direction = 2
        elif direction is 2:  # 왼쪽
            if left < 0: continue
            for i in range(n-1, -1, -1):
                if arr[left][i] != 0:
                    continue
                arr[left][i] = num
                num += 1
            left -= 1
            direction = 3
        elif direction is 3:  # 위
            if up < 0: continue
            for i in range(n-1, -1, -1):
                if arr[i][up] != 0:
                    continue
                arr[i][up] = num
                num += 1
            up += 1
            direction = 0

    # 출력
    print("#%d" % (a+1))
    for line in arr:
        print(' '.join(map(str, line)))