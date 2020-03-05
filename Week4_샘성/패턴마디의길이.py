t = int(input())

for case in range(t):
    string = input()
    cnt = 1  # 패턴의 길이
    pattern = ""
    flag = False

    while True:
        pattern = string[:cnt]
        # print(pattern, cnt)
        if cnt == 10:
            break
        for i in range(cnt, len(string), cnt):
            if pattern != string[i:i + cnt]:
                break
            else:
                flag = True
                break

        if flag:
            break

        cnt += 1

    print("#%d" % (case+1), len(pattern))