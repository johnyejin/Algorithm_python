import fractions

t = int(input())
dic = {'north': 0, 'west': 90}

for case in range(t):
    string = input()
    cnt = 1  # 문자열에 북이랑 서가 몇번 나왔는지
    answer = 0
    idx = 0

    # 맨 오른쪽에 있는거 먼저 더해주기
    if string[len(string)-1] == 'h':
        idx = len(string) - 6
    else:
        idx = len(string) - 5
        answer += 90

    # 오른쪽부터 왼쪽으로 가야함
    while idx > 0:
        if string[idx] == 'h':
            answer -= 90 / 2**cnt
            idx -= 5
        else:
            answer += 90 / 2 ** cnt
            idx -= 4

        cnt += 1

    print("#%d" % (case+1), fractions.Fraction(answer))