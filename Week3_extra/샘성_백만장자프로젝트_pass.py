t = int(input())

for a in range(t):
    n = int(input())
    future = [int(x) for x in input().strip().split()]
    answer = 0

    while True:
        if len(future) == 0:
            break
        maxPriceIdx = future.index(max(future))
        print(future, maxPriceIdx)

        for i in range(maxPriceIdx):
            answer -= future[i]
        answer += maxPriceIdx * future[maxPriceIdx]
        future = future[maxPriceIdx+1:]


    print("#%d" % (a+1), answer)