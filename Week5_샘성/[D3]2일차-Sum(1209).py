for case in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sumList = []

    # 가로 먼저 계산
    for i in range(100):
        rowSum = 0
        columnSum = 0
        for j in range(100):
            rowSum += arr[i][j]
            columnSum += arr[j][i]
        sumList.append(rowSum)
        sumList.append(columnSum)

    print("#%d" % t, max(sumList))