t = int(input())

for case in range(t):
    n = int(input())
    answer = 0

    for i in range(1, n+1):
        if i % 2 == 1:
            answer += i
        else:
            answer -= i

    print("#%d" % (case+1), answer)