t = int(input())

for a in range(t):
    n = int(input())
    future = [int(x) for x in input().strip().split()]
    answer = 0

    increase = 0
    cnt = 0
    for i in range(1, len(future)):
        # print(cnt, increase, answer)

        if future[i-1] > future[i]:
            if increase != i-1:
                answer += cnt * future[i-1]
            cnt = 0
            increase = i
            continue

        cnt += 1
        answer -= future[i-1]

    if cnt != 0:
        answer += cnt * future[n-1]

    print("#%d" % (a+1), answer)