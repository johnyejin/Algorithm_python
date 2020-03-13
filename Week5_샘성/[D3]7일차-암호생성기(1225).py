for case in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    cycle = 1

    while True:
        if cycle == 6:
            cycle = 1

        if arr[0] - cycle <= 0:
            arr.append(0)
            arr.pop(0)
            break
        arr.append(arr[0] - cycle)
        arr.pop(0)
        cycle += 1

    print("#%d" % t, ' '.join(map(str, arr)))