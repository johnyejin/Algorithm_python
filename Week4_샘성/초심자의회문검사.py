t = int(input())

for case in range(t):
    string = input()
    answer = 1

    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            answer = 0
            break

    print("#%d" % (case+1), answer)