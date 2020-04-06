T = int(input())
for case in range(1, T+1):
    n = int(input())
    name = [input() for _ in range(n)]

    answer = list(set(name))
    answer.sort()

    answer = sorted(answer, key=len)

    print("#%d" % case)
    for ans in answer:
        print(ans)