# 조망권 확보된 빌딩수를 세는게 아니라 세대수를 세는거임!
for case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    for i in range(2, n-2):
        temp = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        if max(temp) < arr[i]:
            answer += arr[i] - max(temp)

    print("#%d" % case, answer)