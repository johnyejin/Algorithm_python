t = int(input())
for case in range(1, t+1):
    num = input()
    cnt = 1  # 게임이 진행된 횟수

    while len(num) != 1:
        num = str(int(num[0]) + int(num[1])) + num[2:]
        cnt += 1


    if cnt % 2 == 0:
        print("#%d" % case, 'A')
    else:
        print("#%d" % case, 'B')