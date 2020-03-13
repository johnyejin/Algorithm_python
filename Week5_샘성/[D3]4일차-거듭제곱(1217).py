def calPow(num, cnt):
    global n, m, answer
    if cnt == m:
        answer = num
        return

    calPow(num * n, cnt + 1)


for case in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())

    calPow(n, 1)
    print("#%d" % t, answer)