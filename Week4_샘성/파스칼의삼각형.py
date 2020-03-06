t = int(input())

for case in range(t):
    n = int(input())
    answer = [[1]]

    for i in range(1, n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(answer[i-1][j-1] + answer[i-1][j])
        answer.append(temp)

    print("#%d" % (case+1))
    for line in answer:
        print(' '.join(map(str, line)))